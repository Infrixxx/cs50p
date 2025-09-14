#!/usr/bin/env python3
import sys
"""
Check if the user inputed a file after executing main
Check if it's a valid filename.
"""

if len(sys.argv) != 2 or not sys.argv[1].endswith(".py"):
    sys.exit("")
