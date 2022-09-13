# Input of the user

mathematical_expression = input("Enter a mathematical expression: ")

# Importing regex library

import math
import re

# Defining the function

def formular(mathematical_expression):
    pattern = r"((-?(?:\d+(?:\.\d+)?))|([-+\/*()])|(-?\.\d+))"
    if not re.match(pattern, mathematical_expression):
        print("false")
    else:
        print("true")

formular(mathematical_expression)