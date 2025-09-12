#!/usr/bin/env python3

from plates import is_valid

def test_vanity():
    assert is_valid("AB123") == True
    assert is_valid("XY7890") == True
    assert is_valid("ZZZ999") == True
    assert is_valid("A1B2") == False
    assert is_valid("B0C") == False
    assert is_valid("9ABC") == False
    assert is_valid("!AB123") == False
    assert is_valid("A") == False
    assert is_valid("LONGPLATE") == False
    assert is_valid("ABC-123") == False
