#!/usr/bin/env python3

def main():
        while True:
            try:
                
                fraction =(input("Fraction: ")).strip()
                percentage=convert(fraction)
                print(gauge(percentage))
            
                break

            except(ValueError, ZeroDivisionError, IndexError):
                continue
            

def convert(fraction):
    x, y = map(int, fraction.split("/")) # split into x and y, convert to int.

    if (x < 0) or (y < 0) or (x > y):
        raise ValueError

    return round((x/y)*100)


def gauge(percentage):
    if percentage >= 99:
        return "F"
    
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__=="__main__":
    main()
