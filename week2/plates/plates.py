#!/usr/bin/env python3

"""
minimum, two character, maximum 6.

Numbers cannot be used in the middle of a plate;
they must come at the end
No periods, spaces, or punctuation marks are allowed.i
"""

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    for i in plate:
        if i=>"A" and i<="Z":
            count+=1
            if count<=6:
                continue
            else:
                break
    return


main()
