"""# Task 1

# Get the length of a variable with len()

text = "Berlin is a world city of culture, politics, media and science."

len(text) 

# Task 2

# To get the first character of a variable use index [0]

text[0]

# To get the last character of a variable use index [-1]

text[-1]

# Task 3

# Using the upper() in-built function makes every character upper

text[:3].upper()



# Task 4

text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital"

# Using the count() function

# Be careful to convert the integer into a string with str()

print("B appears: " + str(text.count("B")) + " times")

# Task 5

from re import T


text = "Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau."

text[-10:]

# Task 6

text = "---Python programming---"

# Removing character from string with using replace()

text = text.replace("---", " ")
print(text)


username = input("Choose a username:")
final_username = username.replace("_", "")

print("Your username is:" + final_username)
"""
# Removing multiple characters using replace() in a loop

username = input("Choose a username:")
disallowed_characters = "._!"

for character in disallowed_characters:
    username = username.replace(character,"")

print("Your username is:" + username)

# Task 7

