#!/usr/bin/env python3
"""
"""
import requests
import sys

if len(sys.argv) > 2 :
    if not sys.arg[1].isnumeric:
        sys.exit("Command-line argument is not a number")

else:
    print("Missing command-line argument")


"""
print(f"the number of arrguments is {len(sys.argv)}")
