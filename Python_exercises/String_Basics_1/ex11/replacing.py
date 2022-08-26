# Replacing a substring in a string if you just want to replace a single word with regex

# Importing re

"""import re

story = "A dogmatic dog buys dogecoin to become rich and buy hotdogs every day."

# Using the substring function sub()

new_string = (re.sub(r"\bdog\b", "cat", story))

print(new_string) 

# Different way using replace function and paying attention to space

text = "A dogmatic dog buys dogecoin to become rich and buy hotdogs every day."

word = text.replace(" dog ", " cat ")
print(word)

new = text.replace(" dog ", " cat ")
print(f"{new}")"""

# Important to pay attention to double quotes and single quotes and spaces!

print(f"{text.replace(' dog ' , ' cat ')}")