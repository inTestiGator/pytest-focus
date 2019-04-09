# -*- coding: utf-8 -*-

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
    group = parser.getgroup('focus')
    group.addoption(
        '--focus',
        action='store_true',
        help='focus: type --focus after pytest.'
    )

def pytest_test():
    if pytest.config.getoption('focus'):
        return "BLAAAAH"
