#!/usr/bin/env python3

"""
pseudo code :

            --->Ask user to input a fruit
            --->strip white spaces from input and make it lowercase.
            --->Assume the user inputs fruit names written the same as in the poster.
            --->make a dictionary of fruits and equate them to key value being the calories
            --->check if the input exists in the said list of fruits
            ---> if it exists, return the calories of the fruit.
                --->return calories
            --->if it doesnt exist, ignore the input.
                --->return false annd exit.
"""

def main():
    calories()

def calories():


    fruit_calories = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80
        }



    fruit=(input("Item: "))

    if fruit not in fruit_calories:
        return False
    else:
        return print(f"Calories : {fruit.title()}":{fruit_calories[fruit]})

if __"name"__=="__main__":
    main()
