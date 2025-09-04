#!/usr/bin/env python3

"""
prompt user for fraction x/y

x has to be positive interger and y too.

Return the value as a percentage rounded to the nearest interger


if >= 99% return F for full

if <=1% return E for empty


Exceptions to take into account:

            # - Non-integer input (ValueError)
            # - Division by zero (ZeroDivisionError)  
            # - Not enough values after split (IndexErro

"""

def main():
    return fraction()

def fraction():
    while True:
        try:
            number=(input("Fraction: ")).strip().split("/")
        
            if number[0].isnumeric and number[1].isnumeric:
                if int(number[0])>=0 and int(number[1])>=0:
                    x=int(number[0])
                    y=int(number[1])
        
                    return print(x,y)
                    
        except(ValueError, ZeroDivisionError, IndexError):
                continue        
        

if __name__=="__main__":
    main()
