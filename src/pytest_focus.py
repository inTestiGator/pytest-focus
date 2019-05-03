# -*- coding: utf-8 -*-
"""
Plug in for pytest that sends push notifications for failed tests
"""

from sys import platform
import pytest
from _pytest.terminal import TerminalReporter


def pytest_addoption(parser):
    """ Sets up plugin option """
    group = parser.getgroup("terminal reporting", "reporting", after="general")
    group._addoption(
        "--instafail",
        action="store_true",
        dest="instafail",
        default=False,
        help=(
            "show failures and errors instantly as they occur (disabled by " "default)."
        ),
    )


@pytest.mark.trylast
def pytest_configure(config):
    """ Coniguration for terminal reporter """
    if hasattr(config, "slaveinput"):
        return
    if config.option.instafail and config.pluginmanager.hasplugin("terminalreporter"):
        standard_reporter = config.pluginmanager.getplugin("terminalreporter")
        instafail_reporter = InstafailingTerminalReporter(standard_reporter)

        config.pluginmanager.unregister(standard_reporter)
        config.pluginmanager.register(instafail_reporter, "terminalreporter")


class InstafailingTerminalReporter(TerminalReporter):
    """ Reports failing test cases as they fail """

    def __init__(self, reporter):
        """ Initilize """
        TerminalReporter.__init__(self, reporter.config)
        self._tw = reporter._tw


def pytest_test():
    """
    the plug-in for pytest
    """
    os_name = "unknown"

    if platform in ("linux", "linux2"):
        os_name = "linux"  # linux
    elif platform == "darwin":
        os_name = "Mac"  # OS X
    elif platform == "win32":
        os_name = "windows"  # Windows...

    return os_name
