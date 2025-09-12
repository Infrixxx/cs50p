#!/usr/bin/env python3

from plates import is_valid

def test_vanity():
    assert is_valid("AB50") == True
    assert is_valid("BCRA90") == True
    assert is_valid("HEAVEN") == True
    assert is_valid("HEA05") == False
    assert is_valid("HEA76B") == False
    assert is_valid("BB07C8") == False
    assert is_valid("123456") == False
    assert is_valid("ABC.PI") == False
    assert is_valid("LONGPLATE") == False
    assert is_valid("ABC-.*") == False
