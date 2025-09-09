#!/usr/bin/env python3

import sys
from pyfiglet import Figlet


#to take the arguments from the system:

print(f"number of arguments is {len(sys.argv)}")

figlet=Figlet()

if sys.argv[1]=="-f" or sys.argv[1]=="--font":
    font_name=sys.argv[2]

if font_name in figlet.getFonts():
    figlet.setFont(font=f)

input_str=input("Input: ")
print(f"Output: {figlet.renderText(input_str)}")
