#!/usr/bin/env python3

from pyfiglet import Figlet

figlet=Figlet()
input_str=input("Input: ")
print(f"Output: {figlet.renderText(input_str)})
