#test code

"""
--->conditions:

1. start with atleast two letters,so [0] and [1] has to be letters
2. minimum length == 2 and maximum character length == 6
3. if number is introduced, at that point till end, there must only be numbers
4. The first number cannot be zero.


Pseudo code:

for characters in input:

    ---> remove all white space first
    ---> ensure all is caps
    --->check if the number of characters is atleast ==2 and at most =6
        ---> if so continue
            --->check if all characters are alphanumeric:
                ---> if so continue to check first two characters
            --->if not, return not a vanity plate.
        --->if not, return it's not a vanity plate

    ---> check if first two characters are letters 
        ---> if not return it's not a vanity plate
        ---> if it is, then continue
    
    --->check after first two characters, if it's a number or letter
        ---> if it's a number, is not = 0
            --->if so continue
                --->check if all characters till last are numbers
                    --->if not, return it's not a vanity plate
                    --->if yes, return it is a vanity plate
            --->if not end, is not vanity plate
        --->if it's a letter continue, until end or until find a number
            --->if find a number go back to check if number is not = 0 step
            --->if no number found and till end, return it is a vanity plate
"""

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


main()
