# Replacing a substring in a string

import re

story = input("Enter the story: ")

new_string = (re.sub(r"\bdog\b", "cat", story))

print(new_string)