# Importing regex library

import re 

'''# Task 1

text = "Berlin is a world city of culture, politics, media and science."

pattern = " " # defining a white space

search_space = re.search(pattern, text)



print(f"The first white-space character is located at position: {search_space}")



# Task 2

text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."

print(re.search("Frankfur", text))


# Task 3 

text = "Berlin is a city of culture."

splitted_text = re.split(" ", text)

print(splitted_text)


# Task 4

text = "Berlin is a city of culture."

x = re.search("in", text)

print(x)


# Task 5

text = "Berlin is a city of culture."

pattern = r"[B]\w+" # Pattern to search for a string which starts with specific character

x = re.match(pattern, text).start() # .start() says the start of the index
y = re.match(pattern, text).end()  # .end() says the end of the index

print(f"{x}, {y}")
'''
# Task 6

text = "The rain in Spain."

pattern = r"ai"

x = re.findall(pattern, text)

print(x)

times = len(re.findall(pattern, text)) # To count a regex pattern mulitple times in a given string, use the method len(re.findall(pattern, string))

print(times)
