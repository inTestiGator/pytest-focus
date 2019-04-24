# -*- coding: utf-8 -*-
"""
Plug in for pytest that sends push notifications for failed tests
"""
import subprocess
import pytest

# def pytest_addoption(parser):
#     group = parser.getgroup('pytest.focus')
#     group.addoption(
#         '--focus',
#         action='store_true',
#         dest='/scripts',
#         default='ptfocus',
#         help='focus: type --focus after pytest.'
#     )
#
#     parser.addini('/test/conftest.py')
#
#
# #@pytest.fixture
# def pytest_script():
#     if pytest.config.getoption('focus'):
#         return "You are going to be focused."
#     #return request.config.option.dest_script


def pytest_addoption(parser):
    """
    add option to find the --focus in the arguments
    """
    group = parser.getgroup("focus")
    group.addoption(
        "--focus",
        action="store_true",
        # help='focus: type --focus after pytest.',
        dest="focus",
        default="False",
        help=("Sends push notifications as tests fails and creates " "todo list"),
    )


def pytest_test():
    """
    the plug-in for pytest
    """
    if pytest.config.getoption("focus"):
        from sys import platform

        if platform == "linux" or platform == "linux2":
            return "WOOOOOO!"  # linux
            subprocess.call("scripts/linux.sh", shell=True)
        elif platform == "darwin":
            return "Mac"  # OS X
        elif platform == "win32":
            return "windows"  # Windows...
