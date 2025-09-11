#!/usr/bin/env python3

"""
func shorten : removes vowels from words

"""

def main():
    vowel_remover()

def shorten(word):
    
    word=word.lower().strip()

    vowels={"a","e","i","o","u"}

    final_word=""

    for i in word:
        if i.lower() in vowels:
            continue
        else:
            final_word+=i

    out=print((f"Output: {final_word}"))

    return out

if __name__=="__main__":
    main()
