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
    return guess()
    
def valid_level():
    while True:
        n=input("Level: ")
    
        if n.isnumeric():
            if int(n) >=1:
                return n
                break
        else:
            continue

n=valid_level()
print(n)

def guess(n):

    answer=random.randit(1,n)
    
    while True:
        
        print("Level: {n}")
        
        try:
            user_guess=input("Guess: ")
            
            if user_guess < answer:
                print("Too small!!")
            elif user_guess > answer:
                print("Too large!")
            else:
                print("Just right!")
                break

        except EOFError:
            break

if __name__=="__main__":
    main()
