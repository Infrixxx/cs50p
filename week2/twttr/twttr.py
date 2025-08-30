#!/usr/bin/env python3

"""
removing the vowels from the input
"""

def main():
    vowel_remover()

def vowel_remover():
    vowels={"a","e","i","o","u"}

    inp=(input("Input: "))
    
    final_word=""

    for i in inp:
        if i.lower() in vowels:
            continue
        else:
            final_word+=i

    out=print(("Output: ")+final_word)

    return

if __name__=="__main__":  
    main()
