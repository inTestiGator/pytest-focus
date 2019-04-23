# -*- coding: utf-8 -*-
from pytest_focus import pytest_test

def test_something():
    test = pytest_test()
    assert test == "WOOOOOO"
