#!/usr/bin/env python3
"""
prompts the user for items:
    one per line
    until user inputs "ctrl+d"
    output user’s grocery list in all uppercase
    sorted alphabetically by item
    prefix each line with a number of items the user inputted.
    No need to pluralize the items.

    User input case insensitively.

Pseudo code:
    
    create an empty dictionary
    when the user enters an item, assign the item to the dictionary with a value.
    everytime the user enters an item, check if it's in the dictionary.
        --> if it is in the dictionary, add to the value of the item in the dictionary.
        --> if it is not in the dictionary, initialize it to one.
    
    sort the keys in alphabetical order.
    
    return the number, with prefix of number of items, user inputted.

    user input is case insensitive.
    
    do this until we reach the end of the file "user inputs ctrl-d"

"""

def main():
    return grocery()

def grocery():

    food_list={}
    while True:
        try:
            item=input("").lower().strip()

            if item in food_list:
                food_list[item]+=1
            else:
                food_list[item]=1

        except(EOFError):
            break

        sorted_items = sorted(food_list.keys())

        for item in sorted_items:
            print(f"food_list[item] {item.upper()}
