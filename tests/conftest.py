"""Configuration file for the test suite"""
import os
import sys
import pytest
from _pytest.terminal import TerminalReporter
from sys import platform
from win10toast import ToastNotifier


GO_BACK_A_DIRECTORY = "/../"
GO_INTO_SRC_DIRECTORY = "src"
# pytest_plugins = 'pytester'

# set the system path to contain the previous directory
PRE_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PRE_DIRECTORY + GO_BACK_A_DIRECTORY + GO_INTO_SRC_DIRECTORY)


# def pytest_addoption(parser):
#     """Parser adoption to allow plugin to be run with --focus flag."""
#     group = parser.getgroup("focus")
#     group.addoption(
#         "--focus", action="store_true", help="focus: type --focus after pytest"
#     )

def mac_notify(title, subtitle, message):
    t = "-title {!r}".format(title)
    s = "-subtitle {!r}".format(subtitle)
    m = "-message {!r}".format(message)
    os.system(
        'terminal-notifier {} -activate "com.apple.Terminal"'.format(
            " ".join([m, t, s])
        )
    )
    sys.stdout.write("It appears you have failing test cases...\n")


def win_notify(title, message):
    toast = ToastNotifier()
    toast.show_toast(title, message)


def linux_notify(title, message):
    os.system("notify-send {} --urgency=critical".format(" ".join([title, message])))

# The notifier function
def notify(title, subtitle, message):
    """ Send a notification to the user's screen """
    if platform == "darwin":
        mac_notify(title, subtitle, message)
    elif platform in ("linux", "linux2"):
        print("Failures!")
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
        focus_reporter = focusingTerminalReporter(standard_reporter)

        config.pluginmanager.unregister(standard_reporter)
        config.pluginmanager.register(focus_reporter, "terminalreporter")
        # mac_notify()


class focusingTerminalReporter(TerminalReporter):
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
            notify("Title", "Subtitle", "Message")
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



PYTEST_PLUGINS = "pytester"
