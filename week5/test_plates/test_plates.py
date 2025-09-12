#!/usr/bin/env python3

from plates import is_valid

def test_vanity():
    assert is_valid("ABS578") == True
    assert is_valid("BCR057") == False
    assert is_valid("BC") == True
    assert is_valid("BC078B") == False
    assert is_valid("071") == False
    assert is_valid("ABBCCC") == True
    assert is_valid("!@#$%") == False
    assert is_valid("tylo75489") == False
    assert is_valid("CS50") == True
    assert is_valid("ECTO88") == True
    assert is_valid("NRVOUS") == True
    assert is_valid("CS05") == False
    assert is_valid("CS50P2") == False
    assert is_valid("123456") == False
    assert is_valid("PI3.14") == False
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False
    assert is_valid("ABC?!-") == False
