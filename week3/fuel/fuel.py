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
            x=int(number[0])
            y=int(number[1])
            if x > y:
                continue #the numerator cannot be bigger than the denominator, so ask again
                        
            percentage=((x/y)*100)
            percentage=round(percentage,0)
            percentage=int(percentage)

            if percentage >= 99:
                return print("F")
            elif percentage <= 1:
                return print("E")
            else:
                return print(str(percentage)+"%")
        except(ValueError, ZeroDivisionError, IndexError):
                continue        
        

if __name__=="__main__":
    main()
