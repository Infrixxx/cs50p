#!/usr/bin/env python3
import random

"""
Prompts the user for a level(n)
Generate a random number between 1 and n, inclusive
If guess is negative, prompt the user again

Conditions:
    ---> if guess < n, output "Too small!!" prompt the user again
    ---> if guess > n, output "Too large!" prompt the user again
    ---> if guess is same as n, "Just right!" and exit
"""

def main():

def guess(n):
    
    while True:
        try:
            n=input("Level: ")
            
            if n < rn:
                print("Too small!!")
            elif n > rn:
                print("Too large!")
            else:
                print("Just right!")
                break

        except EOFError:
            break


