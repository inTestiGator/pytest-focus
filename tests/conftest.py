"""Configuration file for the test suite"""
import os
import sys

GO_BACK_A_DIRECTORY = "/../"
GO_INTO_SRC_DIRECTORY = "src"
# pytest_plugins = 'pytester'

# set the system path to contain the previous directory
PREVIOUS_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PREVIOUS_DIRECTORY + GO_BACK_A_DIRECTORY + GO_INTO_SRC_DIRECTORY)

def pytest_addoption(parser):
    group = parser.getgroup('focus')
    group.addoption(
        '--focus',
        action='store_true',
        help='focus: type --focus after pytest.'
    )

pytest_plugins = 'pytester'
