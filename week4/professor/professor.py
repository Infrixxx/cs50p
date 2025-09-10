#!/usr/bin/env python3
import random

"""
Calculator game:
    generates random equations
    Waits for input from user
    If the user enters incorrect input it returns "EEE"
    After 3 tries, it returns the correct answer.

    prompts the user for level between 1-3, inclusive. (return value error if neither)
    
    x + y format
    n=level is the number of digit
    return user score at end, number of correct answers
"""

def main():
    level=get_level()
    score=0

    for q in range(10):
        x=generate_integer(level)
        y=generate_integer(level)
        score+=ask(x,y)
    print(f"Score: {score}")
        
    
    
    
def get_level():
    while True:
        try:
            level=input("Level: ")
            
            if level in ['1','2','3']:
                return int(level)
                break
        except ValueError:
             continue
            

def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2 :       
        return random.randint(10,99)
    else:
        return random.randint(100,999)
            
def ask(x, y):
    correct = x + y
    for a in range(3):
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == correct:
                return 1
        except ValueError:
            pass
        print("EEE")
    print(f"{x} + {y} = {correct}")
    return 0


if __name__=="__main__":
    main()
