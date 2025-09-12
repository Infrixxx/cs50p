#!/usr/bin/env python3

from plates import is_valid

def test_vanity():
    assert is_valid("AB") == True
    assert is_valid("XY7890") == True
    assert is_valid("ZZZ999") == True
    assert is_valid("12BB") == False
    assert is_valid("B0CCAR") == False
    assert is_valid("BB078") == False
    assert is_valid("--AB12") == False
    assert is_valid("A") == False
    assert is_valid("LONGPLATE") == False
    assert is_valid("ABC-123") == False
