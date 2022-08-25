# How to check if the length of a word is odd or even

word = str(input("Enter a word: "))

if len(word)%2 == 0:
    print(f"The string '{word}' has an even number of characters.")
elif len(word)%2 != 0:
    print(f"The string '{word}' has an odd number of characters.")
elif len(word) == "":
    print("The string has an even number of characters.")
else:
    print("Something went wrong, try again!")