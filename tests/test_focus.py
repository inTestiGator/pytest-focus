# -*- coding: utf-8 -*-
from pytest_focus import pytest_test

def test_something():
    tset = pytest_test()
    assert tset == "BLAAAAH"
