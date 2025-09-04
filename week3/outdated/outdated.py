#!/usr/bin/env python3

"""
I need to take a date in 

month/day/year and set it to YYYY-MM-DD

So it can be in format of MM/DD/YYYY
or
Month_as_word DD, YYYY 
"""

def main():
    return date()

def date():

    months={
    "January":1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12
    }

    while True:
        mm, dd, yy = input("Date: ").strip().split("/")  #MM/DD/YYYY
        mm, dd, yy = int(mm), int(dd), int(yy)

        return print(f"{yy}-{mm:02d}-{dd:02d}")

if __name__=="__main__":
    main()
