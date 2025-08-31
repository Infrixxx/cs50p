#!/usr/bin/env python3

"""
minimum, two character, maximum 6.

Numbers cannot be used in the middle of a plate;
they must come at the end
No periods, spaces, or punctuation marks are allowed.
"""

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check length first
    if len(s) < 2 or len(s) > 6:
        return False
    
    # Check first two characters are letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    
    # Check all characters are alphanumeric
    for char in s:
        if not char.isalnum():
            return False
    
    # Check numbers are only at the end and first number isn't '0'
    found_number = False
    for char in s:
        if char.isdigit():
            if not found_number and char == '0':
                return False  # First number can't be '0'
            found_number = True
        elif found_number:
            return False  # Letter after number is invalid
            
    return True

if __name__ == "__main__":
    main()
