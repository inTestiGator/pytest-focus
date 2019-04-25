# -*- coding: utf-8 -*-
"""
Plug in for pytest that sends push notifications for failed tests
"""
import subprocess
import pytest
from sys import platform

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
