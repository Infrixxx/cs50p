#!/usr/bin/env python3

"""
prompts the user for a string in English
Outputs the emojized version, of the string.
use the emoji library to do this.
"""

import emoji

input_str=input("Input: ").strip()
emojized= emoji.emojize(input_str,language="alias")
print(f"Output: {emojized} ")
