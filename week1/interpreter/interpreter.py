
#!/usr/bin/env python3

"""
A program that 
--> prompts the user for an arithmetic expression
--> calculates the result 
--> outputs as a floating-point value
"""

user_expression = input("Expression: ")

parts = user_expression.strip().split() #remove white space and also split into arrayi
x, y, z = parts

num1 = float(x)
num2 = float(z)

if y == '+':
    result = num1 + num2
elif y == '-':
    result = num1 - num2
elif y == '*':
    result = num1 * num2
elif y == '/':
    result = num1 / num2

print(result)
