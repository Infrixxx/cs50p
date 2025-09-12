#!/usr/bin/env python3

from bank import value

def test_value():
    assert value("Hello") == "$0"
    assert value("Hy") == "$20"
    assert value("Dumela") == "$100"
