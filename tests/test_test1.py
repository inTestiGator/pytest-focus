from test1 import *


def test_iequals1():
    i = iequals1()
    assert i == 1

def test_iequals2():
    i = iequals2()
    assert i == 2

def test_fail_test():
    i = fail_test()
    assert i == 0
