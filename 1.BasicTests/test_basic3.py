from functions import *

def test_valid_email():
    assert valid_email("example@domain.com") is True
    assert valid_email("example.com") is False

def test_divide():
    assert divide(4,2) == 2
    assert divide(4,0) is None
