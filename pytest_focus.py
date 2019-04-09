# -*- coding: utf-8 -*-

import pytest


def pytest_addoption(parser):
    group = parser.getgroup('focus')
    group.addoption(
        '--script',
        action='store',
        dest='dest_script',
        default='ptfocus',
        help='Set the script for the fixture "script".'
    )

    parser.addini('HELLO', 'Dummy pytest.ini setting')


@pytest.fixture
def script(request):
    return request.config.option.dest_script
