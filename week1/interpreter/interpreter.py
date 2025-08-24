
#!/usr/bin/env python3

"""
A program that 
--> prompts the user for an arithmetic expression
--> calculates the result 
--> outputs as a floating-point value
"""

user_expression=input("Expression: ")

no_white=user_expression.strip() #remove white spaces.
x,y,z=no_white.split(" ")

print(x)
print(y)
print(z)
