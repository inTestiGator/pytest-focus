@pytest.mark.XFAIL
def test_fail():
    a = 2
    assert a == 3


def test_pass():
    a = 3
    assert a == 3

@pytest.mark.XFAIL
def test_fail1():
    a = 2
    assert a == 3


def test_pass1():
    a = 3
    assert a == 3


def test_pass2():
    a = 3
    assert a == 3


def test_pass3():
    a = 3
    assert a == 3


def test_pass4():
    a = 3
    assert a == 3


def test_pass5():
    a = 3
    assert a == 3


def test_pass6():
    a = 3
    assert a == 3


def test_pass7():
    a = 3
    assert a == 3

@pytest.mark.XFAIL
def test_fail2():
    a = 2
    assert a == 3
