"""
Test cases designed to see if plugin works
"""

import pytest


#@pytest.mark.xfail
def test_fail():
    """ Failing test """

    a = 2
    assert a == 3


def test_pass():
    """ Passing test """
    a = 3
    assert a == 3


#@pytest.mark.xfail
def test_fail1():
    """ Failing test """
    a = 2
    assert a == 3


def test_pass1():
    """ Passing test """
    a = 3
    assert a == 3


def test_pass2():
    """ Passing test """
    a = 3
    assert a == 3


def test_pass3():
    """ Passing test """
    a = 3
    assert a == 3


def test_pass4():
    """ Passing test """
    a = 3
    assert a == 3


def test_pass5():
    """ Passing test """
    a = 3
    assert a == 3


def test_pass6():
    """ Passing test """
    a = 3
    assert a == 3


def test_pass7():
    """ Passing test """
    a = 3
    assert a == 3


@pytest.mark.xfail
def test_fail2():
    """ Failing test """
    a = 2
    assert a == 3
