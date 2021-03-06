# -*- coding: utf-8 -*-
"""
Plug in for pytest that sends push notifications for failed tests
"""
import os
import sys
from sys import platform
import pytest
from _pytest.terminal import TerminalReporter

if platform == "win32":
    from win10toast import ToastNotifier


def mac_notify(title, subtitle, message):
    """ Handles Mac Notification """
    push_t = "-title {!r}".format(title)
    push_s = "-subtitle {!r}".format(subtitle)
    push_m = "-message {!r}".format(message)
    os.system(
        'terminal-notifier {} -activate "com.apple.Terminal"'.format(
            " ".join([push_m, push_t, push_s])
        )
    )
    sys.stdout.write("It appears you have failing test cases...\n")


def win_notify(title, message):
    """ Handles windows notifications """
    toast = ToastNotifier()
    toast.show_toast(title, message)


def linux_notify(title, message):
    """ Handles linux notifications """
    os.system("notify-send {} -u critical".format(" ".join([title, message])))


# The notifier function
def notify(title, message, subtitle="Test Case Failed."):
    """ Send a notification to the user's screen """
    if platform == "darwin":
        mac_notify(title, subtitle, message)
    elif platform in ("linux", "linux2"):
        linux_notify(title, message)
    elif platform == "win32":
        win_notify(title, message)


def pytest_addoption(parser):
    """ Sets up plugin option """
    # pylint: disable=protected-access
    group = parser.getgroup("terminal reporting", "reporting", after="general")
    group._addoption(
        "--focus",
        action="store_true",
        dest="focus",
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
    if config.option.focus and config.pluginmanager.hasplugin("terminalreporter"):
        standard_reporter = config.pluginmanager.getplugin("terminalreporter")
        focus_reporter = FocusingTerminalReporter(standard_reporter)

        config.pluginmanager.unregister(standard_reporter)
        config.pluginmanager.register(focus_reporter, "terminalreporter")


class FocusingTerminalReporter(TerminalReporter):
    """ Reports failing test cases as they fail """

    def __init__(self, reporter):
        """ Initilize """
        # pylint: disable=protected-access
        TerminalReporter.__init__(self, reporter.config)
        self._tw = reporter._tw

    def pytest_collectreport(self, report):
        """ Live errors during test suite run """
        TerminalReporter.pytest_collectreport(self, report)
        if report.failed:
            if self.isatty:
                self.rewrite("")
            self.print_failure(report)

    def pytest_runtest_logreport(self, report):
        """ Shows failures and errors as tests are running """
        TerminalReporter.pytest_runtest_logreport(self, report)
        if report.failed and not hasattr(report, "wasxfail"):
            if self.verbosity <= 0:
                self._tw.line()
            self.print_failure(report)

    def print_failure(self, report):
        """ sends push notifications as test cases fail """
        if self.config.option.tbstyle != "no":
            if self.config.option.tbstyle == "line":
                line = self._getcrashline(report)
                self.write_line(line)
            else:
                msg = self._getfailureheadline(report)
                when = getattr(report, "when", "collect")
                if when == "collect":
                    msg = "ERROR collecting " + msg
                elif when == "setup":
                    msg = "ERROR at setup of " + msg
                elif when == "teardown":
                    msg = "ERROR at teardown of " + msg
                self.write_sep("_", msg)
                if not self.config.getvalue("usepdb"):
                    self._outrep_summary(report)
