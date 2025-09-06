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
             ":1st_place_medal:":"🥇",
             ":thumbs_up:":"👍",
             ":ear:":"👂",
             "candy:":"🍬",
             ":cooked_rice:":"🍚",
             ":ice_cream:":"🍨"}
        key=input("Input: ")
        keys=key.strip().split() 
        output=[] 
        for key in keys:
            if key in emojis:
                output.append(emojis[key])
            else:
                continue

        return print(f"Output: {output}") 
    except (KeyError):
        return False
if __name__=="__main__":
    main()
