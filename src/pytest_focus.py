# -*- coding: utf-8 -*-
"""
Plug in for pytest that sends push notifications for failed tests
"""
import subprocess
import pytest


def pytest_addoption(parser):
    group = parser.getgroup('focus')
    group.addoption(
        '--focus',
        action='store_true',
        # help='focus: type --focus after pytest.',
        dest='focus',
        default='False',
        help=(
            'Sends push notifications as tests fails and creates '
            'todo list'
        )
    )


def pytest_test():
    """
    the plug-in for pytest
    """
    if pytest.config.getoption("focus"):
        from sys import platform
        if platform == "linux" or platform == "linux2":
            print ("WOOOOOO!")  # linux
            subprocess.call("src/scripts/linux.sh", shell=True)
        elif platform == "darwin":
            return "Mac"  # OS X
        elif platform == "win32":
            return "windows"  # Windows...
