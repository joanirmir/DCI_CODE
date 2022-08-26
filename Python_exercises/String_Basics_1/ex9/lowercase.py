# Define a function to lowercase a string

# Defining user input

sentence = input("Enter a sentence: ")

def normalize(sentence):
    if sentence.isupper():
        sentence_new = sentence[0].capitalize() + sentence[1:].lower() + "!"
        print(sentence_new)
    else:
        print(sentence[0].capitalize() + sentence[1:] + ".")

normalize(sentence)

"""
# How to convert uppercase to lowercase with for loop

s = input("Enter a sentence: ")
new_str=""
for i in range (len(s)):
    if s[i].isupper():
        new_str+=[i].lower() # lower() not works for lists
    elif s[i].islower():
        new_str+=s[i].upper()
    else:
        new_str+=s[i]
print(new_str)
"""


