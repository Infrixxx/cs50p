#!/usr/bin/env python3

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    s=s.strip()
    s=s.upper()

    if len(s)>=2 and len(s)<=6:
        if s[0]>="A" and s[0]<="Z" and  s[1]>="A" and s[1]<="Z":
            if not s.isalnum():
                return False
            else:
                if not (s[0] and s[1]).isalpha():
                    return False
                else:
                    for i in range(2,len(s)):
                        if s[i].isnumeric():
                            if s[i]=="0":
                                return False
                            else:
                                if not s[i:].isnumeric():
                                        return False
                                break
                    return True
        else:
            return False
    else:
        return False

if __name__=="__main__":
    main()
