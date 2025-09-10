#!/usr/bin/env python3
"""
request user bitcoin ammount from command line
check if it can be converted to float
if not sys.exit("Command-line argument is not a number")
if no argument sys.exit("Missing command-line argument")
"""
import requests
import sys


if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")

bitcoin_amount=argv[1]

if len(sys.argv) > 2 :
    if not bitcoin_amount.isnumeric:
    sys.exit("Command-line argument is not a number")




"""
print(f"the number of arrguments is {len(sys.argv)}")
