#!/usr/bin/env python3
"""
Expects one command line argument ( name of a csv file or path)
Outputs table formatted as Ascii art using tabulate
Format table using grid format.

conditions:
    if the user doesn't specify one command line argument or if the specified filename doesnt end with      csv, or the file doesn't not exist, program should exit via sys.exit
"""

import sys
import csv
import tabulate

if len(sys.argv) < 2 :
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 2 :
    sys.exit("Too many command-line arguments")

filename=sys.argv[1]

if not filename].endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    with open(filename,r ) as file:
        lines=file.readline()
except FileNotFoundError:
    sys.exit("File Does not exist")
