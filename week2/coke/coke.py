#!/usr/bin/env python3

"""

"""

def main():
    due()


def due():

    am_due=50

    while am_due != 0:
        if am_due >=0:
            show=print("Amount Due: "+str(am_due))
            pay=(input("Insert coin: "))
            am_due=int(am_due)-int(pay)
        else:
            Change=print("Change Owed: " + str(am_due))
            break

if __name__=="__main__":
    main()
