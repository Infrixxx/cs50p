#!/usr/bin/env python3

import sys
from pyfiglet import Figlet

figlet=Figlet()

if len(sys.argv == 3):
#to take the arguments from the system:

    if sys.argv[1]=="-f" or sys.argv[1]=="--font":
        font_name=sys.argv[2]
    
        if font_name in figlet.getFonts():
            figlet.setFont(font=f)
        else:
            print("Invalid font")
            sys.exit(1)
else:

input_str=input("Input: ")
print(f"Output: {figlet.renderText(input_str)}")
