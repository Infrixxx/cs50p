#!/usr/bin/env python3

"""
Prompt user for name
Repeat until user terminates with ctrl-d
"""

def main():
    return adieu()

def adieu():
    
    #function variables:

    names=[]
    output_str=""
    
    #function code:

    while True:
        try:
            name=input("Name: ").strip()
            names.append(name)
        except(EOFError):
            break
        fin_indx=len(names)-1

        for name in names:
            if fin_indx > 1:
                output_str=", ".join(names[:-1]) + f" and {names[-1]}"
            elif fin_indx==1:
                output_str=f"{names[0]} and {names[1]}"
            else:
                output_str=name[0]
    return print(f"Adieu, adieu, to {output_str}")

if __name__=="__main__":
    main()

