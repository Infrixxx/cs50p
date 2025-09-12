#!/usr/bin/env python3

from plates import is_valid

def test_vanity():
    assert is_valid("ABS578") == True
    assert is_valid("BCR057") == False
    assert is_valid("BC") == True
    assert is_valid("BC078B") == False
