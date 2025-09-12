#!/usr/bin/env python3

from plates import is_valid

def test_vanity():
    assert is_valid("ABS578") == True
    assert is_valid("BCP991") == True
    assert is_valid("ABBCCC") == True
    assert is_valid("BC09") == False
    assert is_valid("BC50R2") == False
    assert is_valid("0715") == False
    assert is_valid("BCR.09") == False
    assert is_valid("B") == False
    assert is_valid("BCR?.-") == False
    assert is_valid("ECOPLANET") == False
