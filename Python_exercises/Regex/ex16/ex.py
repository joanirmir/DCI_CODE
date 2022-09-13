# Create a function that makes a sentence containing sad face and turn them into happy ones

import re

user_input = input("Enter a sentence with a sad smiley: ")

def happy_face(user_input):
    pattern = r"[(]$"
    if re.match(pattern, user_input):
        print(re.sub(pattern, ")", user_input))
    else:
        print(user_input)

happy_face(user_input)