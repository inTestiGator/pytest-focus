"""
practice test cases for testing plugin
"""
from test1 import iequals1
from test1 import iequals2
from test1 import fail_test


def test_iequals1():
    """
    practice test case 1 for testing plugin
    """
    i = iequals1()
    assert i == 1


def test_iequals2():
    i = iequals2()
    assert i == 2


def test_fail_test():
    i = fail_test()
    assert i == 0
