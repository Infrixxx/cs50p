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

    return print(number)

if __name__=="__main__":
    main()
