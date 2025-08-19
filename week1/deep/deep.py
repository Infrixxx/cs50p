#!/usr/bin/env python3

"""
Asks the user what is the great question of life, conditions:

if user types 42 ---> Yes

if user types forty-two ---> yes (case insensitive)

if user types forty two---> yes (case insensitive)

else ---> no

"""

question=input("What is the Answer to the Great Question of Life, the Universe, and Everything?").lower()

if question=="forty-two" or question=="forty two" :

    print("Yes")

elif question=="42":

    print("Yes")

else:

    print("No")
