# -*- coding: utf-8 -*-
"""
Plug in for pytest that sends push notifications for failed tests
"""

from sys import platform


def pytest_test():
    """
    the plug-in for pytest
    """
    os_name = "unknown"

    if platform in ('linux', 'linux2'):
        os_name = "linux"  # linux
    elif platform == "darwin":
        os_name = "Mac"  # OS X
    elif platform == "win32":
        os_name = "windows"  # Windows...

    return os_name
