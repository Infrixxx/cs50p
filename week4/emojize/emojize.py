#!/usr/bin/env python3

"""
prompts the user for a string in English
Outputs the emojized version, of the string.
"""

def main():
    return emojize()

def emojize():
    try:
        emojis={
             ":1st_place_medal:":"🥇",
             ":thumbs_up:":"👍",
             ":ear:":"👂",
             ":candy:":"🍬",
             ":cooked_rice:":"🍚",
             ":ice_cream:":"🍨"}
        key=input("Input: ")
        keys=key.strip().split() 
 
        for i,key in enumerate(keys):
            if key in emojis:
                keys[i]=emojis[key]
        
        output_str=" ".join(keys)
        return print(f"Output: {output_str}") 
    except (KeyError):
        return False
if __name__=="__main__":
    main()
