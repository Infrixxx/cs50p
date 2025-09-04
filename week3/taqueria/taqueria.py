#!/usr/bin/env python3

"""
a program that enables a user to place an order
prompting them for items
one per line
until the user inputs control-d

After each inputted item, display the total cost of all items inputted
prefixed with a dollar sign ($) and formatted to two decimal places.
Treat the user’s input case insensitively.

Assume that every item on the menu will be titlecased
"""

def main():
    return total()

def total():

    menu={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }

    total=0
    
    while True:
        try:
            food=(input()).strip().lower().title()
    
            if food in menu:
                total+=menu[food]
                print(f"${total.2f}")
        except(EOFerror):
            break
if __name__=="__main__":
    main()
