# Importing regex library

import re 

# Task 1

text = "Berlin is a world city of culture, politics, media and science."

pattern = " "

print(f"The first white-space character is located at position: {re.findall(pattern,text)}")