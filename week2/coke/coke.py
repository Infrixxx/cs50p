#!/usr/bin/env python3

"""
Coke is 50 cents

only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

if it's not accepted denomination, ignore
"""

def main():
    due()


def due():

    am_due=50

    while am_due >= 0:
        if am_due > 0:
            show=print("Amount Due: "+str(am_due))
            pay=int((input("Insert coin: ")))
            if ( pay == 25 or pay == 10 or pay == 5):
                am_due=int(am_due)-int(pay)
                        elif am_due==0:
                            print("Change Owed: " + str(am_due))
                            break
                        elif am_due < 0:
                            Change=print("Change Owed: " + str(int(am_due)*-1))
                            break
            else:
                continue

if __name__=="__main__":
    main()
