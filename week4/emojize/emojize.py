#!/usr/bin/env python3

"""
prompts the user for a str in English
Outputs the emojized veraion, of the string.
"""

def main():
    return emojize()

def emojize():
    try:
        emojis={
             ":1st_place_medal:":"🥇"
                }
        key=input("Input: ")

        return print(f"Output: {emojis[key]}") 
    except (KeyError):
        return False
if __name__=="__main__":
    main()
