# -*- coding: utf-8 -*-
"""
Plug in for pytest that sends push notifications for failed tests
"""
import subprocess
import pytest
from sys import platform


def pytest_addoption(parser):
    """pytest addoption parser for reading --focus flag."""
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
    if platform in ('linux', 'linux2'):
        subprocess.call("src/scripts/linux.sh", shell=True)
        return "linux"  # linux
    elif platform == "darwin":
        return "Mac"  # OS X
    elif platform == "win32":
        return "windows"  # Windows...
    else:
        return "unknown"
