#!/usr/bin/env python3

from twttr import shorten

def test_shorten():
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""
    assert shorten("Who are you?") == "Wh r y?"
