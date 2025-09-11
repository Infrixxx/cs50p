#!/usr/bin/env python3

"""
func shorten : removes vowels from words

"""

def main():
    vowel_remover()

def shorten(word):

    vowels_l={"a","e","i","o","u"}
    vowels_u={"A","E","I","O","U"}
    final_word=""

    for i in word:
        if i in vowels_l:
            continue
        elif i in vowels_u:
            continue
        else:
            final_word+=i

    out=print((f"Output: {final_word}"))

    return out

if __name__=="__main__":
    main()
