import pytest
from file1 import square,circle

def test_valid(): 
    assert square(5) == (25,20)
    

# def test_fail():
#     assert square(5) == (78.5397,25)

def test_fail(): 
    assert circle(4) == (16,16)
    

# def test_fail():
#     assert square(5) == (78.5397,31.4159)
    