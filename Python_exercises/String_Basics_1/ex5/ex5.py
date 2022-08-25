

user = input("Put in a single word: ")

# Defining a list with all the vowels

#vowel_list = ["a", "e", "i", "o", "u"]

vowel_list = "aeiou"

# De

"""def inator(user):

    if user[-1] in vowel_list:
        print(f"{user}-inator {str(len(user))}000")
    else:
        print(user + "inator" + str(len(user)) + "000")"""
    


def inator(user):

    if user[-1] in vowel_list:
        print(f"{user}-inator {str(len(user))}000")
    else:
        print(user + "inator" + str(len(user)) + "000")
    


inator(user)