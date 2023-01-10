import pytest

from calculator import sqaure

def test_positive():
    assert sqaure(2) == 4
    assert sqaure(3) == 9


def test_negative():
    assert sqaure(-2) == 4
    assert sqaure(-3) == 9


def test_zero():
    assert sqaure(0) == 0


def test_str():
    with pytest.raises(TypeError):
        sqaure("cat")