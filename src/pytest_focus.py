# -*- coding: utf-8 -*-
""" Creates environment that promotes focused work through various restrictions """

import pytest

def pytest_addoption(parser):
    """ Sets up framework for pytest plug-in """
    group = parser.getgroup('focus')
    group.addoption(
        '--foo',
        action='store',
        dest='dest_foo',
        default='2019',
        help='Set the value for the fixture "bar".'
    )

    parser.addini('HELLO', 'Dummy pytest.ini setting')


@pytest.fixture
def bar(request):
    """ Does nothing """
    return request.config.option.dest_foo
