#!/usr/bin/env python3

"""
if greeting is hello = $0
if greeting :
                ---> starts with H(case insensitive)
                ---> is not hello
                
                get = $20

else:
     ----> if none of the conditions above are met

     get = $100


N.B

    ignore any leading white space

    The input is case insensitive.
"""

greeting=input("Greeting: ").strip().lower()

if greeting=="hello":
    print("$0")
elif greeting[0]=="h":
    print("$20")
else:
    print("$100")


