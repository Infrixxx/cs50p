#!/usr/bin/env python3

"""
prompt user for fraction x/y

x has to be positive interger and y too.

Return the value as a percentage rounded to the nearest interger


if >= 99% return F for full

if <=1% return E for empty

"""

def main():
    return fraction()

def fraction():
    number=(input("Fraction: ")).strip().split("/")

    if number[0].isnumeric and number[1].isnumeric:
        if int(number[0])>=0 and int(number[1])>=0:
            x=int(number[0])
            y=int(number[1])

            return print(x,y)



if __name__=="__main__":
    main()
