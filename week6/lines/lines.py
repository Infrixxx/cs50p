#!/usr/bin/env python3
import sys
"""
Check if the user inputed a file after executing main
Check if it's a valid filename.
"""

if len(sys.argv) != 2 or not sys.argv[1].endswith(".py"):
    sys.exit("Invalid arguments")

try:
    with open(sys.argv[1]) as f:
        print(sum( 1 for line in f if line.strip() and not line.Istrip().startswith("#")))
except FileNotFoundError:
    sys.exit("File does not exist.")
