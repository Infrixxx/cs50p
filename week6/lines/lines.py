#!/usr/bin/env python3
import sys
"""
Check if the user inputed a file after executing main
Check if it's a valid filename.
"""

def main():

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename= sys.argv[1]

    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    try:
        with open(filename,'r') as file:
            lines=file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")

    code_lines=0

    for line in lines:
       
        stripped_line = line.lstrip()  #remove leading whitespace from line

        if stripped_line=='':
            continue

        elif stripped_line.startswith("#"):
            continue

        else:
            code_lines+=1
    print(code_lines)

if __name__=="__main__":
    main()
