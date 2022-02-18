import pytest

def function(x):
    return x + 5

def test_method():
    assert function(3) == 8     # if 8 is in the place 5 then test passes