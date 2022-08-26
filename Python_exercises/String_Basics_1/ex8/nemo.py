"""# Example with given string

given_string = "hello, this text is about a fish that swims in the sea and his name is Nemo, the fish is "
nemo = given_string.find("Nemo") # index 71

print(nemo)

print("I found Nemo at", given_string.find("Nemo"))"""

# Defining a user input

user = input("Enter a string: ")
if "Nemo" in user:
    print("I found Nemo at", user.find("Nemo"))
elif "Nemo" not in user:
    print("I can't find Nemo :(")
else:
    print("Start again")

