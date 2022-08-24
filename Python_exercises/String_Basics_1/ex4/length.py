word = input("Enter a word: ")

if len(word)%2 == 0:
    print("The string has an even number of characters.")
elif len(word)%2 != 0:
    print("The string has an odd number of characters.")
elif len(word) == "":
    print("The string has an even number of characters.")
else:
    print("Something went wrong, try again!")