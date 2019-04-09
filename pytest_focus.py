# -*- coding: utf-8 -*-

import pytest


def pytest_addoption(parser):
    group = parser.getgroup('focus')
    group.addoption(
        '--focus',
        action='store_true',
        dest='/scripts',
        default='ptfocus',
        help='focus: type --focus after pytest.'
    )

    parser.addini('/test/conftest.py')


@pytest.fixture
def script(request):
    return request.config.option.dest_script
