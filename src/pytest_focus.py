# -*- coding: utf-8 -*-
"""
Plug in for pytest that sends push notifications for failed tests
"""

import os.subprocess

from sys import platform
from _pytest.terminal import TerminalReporter

def pytest_addoption(parser):
    group = parser.getgroup("terminal reporting", "reporting", after="general")
    group._addoption(
        '--instafail', action="store_true", dest="instafail", default=False,
        help=(
            "show failures and errors instantly as they occur (disabled by "
            "default)."
        )
    )


@pytest.mark.trylast
def pytest_configure(config):
    if hasattr(config, 'slaveinput'):
        return
    if config.option.instafail and config.pluginmanager.hasplugin('terminalreporter'):
        standard_reporter = config.pluginmanager.getplugin('terminalreporter')
        instafail_reporter = InstafailingTerminalReporter(standard_reporter)

        config.pluginmanager.unregister(standard_reporter)
        config.pluginmanager.register(instafail_reporter, 'terminalreporter')


class InstafailingTerminalReporter(TerminalReporter):
    def __init__(self, reporter):
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
