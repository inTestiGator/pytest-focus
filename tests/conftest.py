"""Configuration file for the test suite"""
import os
import sys
from sys import platform
import webbrowser
import pytest
from _pytest.terminal import TerminalReporter


GO_BACK_A_DIRECTORY = "/../"
GO_INTO_SRC_DIRECTORY = "src"
pytest_plugins = 'pytest_focus'

# set the system path to contain the previous directory
PRE_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PRE_DIRECTORY + GO_BACK_A_DIRECTORY + GO_INTO_SRC_DIRECTORY)

# PYTEST_PLUGINS = "pytester"
