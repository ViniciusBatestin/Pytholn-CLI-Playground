import addition
import pytest

def test_add():
    assert addition.add(4,5) == 9

def test_sub():
    assert addition.sub(10,5) == 5

# return fail

def test_subF():
    assert addition.sub(10,5) == 10
