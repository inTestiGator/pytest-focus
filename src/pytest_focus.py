# -*- coding: utf-8 -*-
"""
Plug in for pytest that sends push notifications for failed tests
"""
import subprocess
import pytest

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
