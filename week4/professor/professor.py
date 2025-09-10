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
    generate_integer(level)
    
def get_level():
    while True:
        try:
            level=input("Level: ")
            
            if level.isnumeric() and int(level) > 0 :

                level=int(level)
            
            if level == 1 or level == 2 or level == 3:
                return level
                break
        except ValueError:
             continue

def generate_integer(level):
    score=0
    
    if level == 1:
        for b in range(10):
            x= random.randint(0,9)
            y= random.randint(0,9)
            
            correct=x+y
    
            for a in range(3):
                answer = input(f"{x} + {y} = ")
                if int(answer) == correct:
                    score+=1
                    break
                else:
                    print("EEE")
            print(f"{x} + {y} = {correct} ")

    elif level == 2 :
        for b in range(10):
            x= random.randint(10,99)
            y= random.randint(10,99)

            correct=x+y
    
            for a in range(3):
                answer = input(f"{x} + {y} = ")
                if int(answer) == correct:
                    score+=1
                    break
                else:
                    print("EEE")
            print(f"{x} + {y} = {correct} ")
            
    else:
        for b in range(10):
            x= random.randint(100,999)
            y= random.randint(100,999)

            correct=x+y
    
            for a in range(3):
                answer = input(f"{x} + {y} = ")
                if int(answer) == correct:
                    score+=1
                    break
                else:
                    print("EEE")
            print(f"{x} + {y} = {correct} ")
                    
    return print(f"Score: {score}")
        
if __name__=="__main__":
    main()
