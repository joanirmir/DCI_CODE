# Create a function that makes a sentence containing sad face and turn them into happy ones

import re

user_input = input("Enter a sentence with a sad smiley: ")

'''def happy_face(user_input):
    pattern = r"(?<=[8;:x])\(" # Positive lookbehind
    happy_smiley = re.sub(pattern, ")", user_input)
    print(happy_smiley)
    #else:
        #print(user_input)

happy_face(user_input)'''



def happy_face(user_input):
    pattern = r"[8;:x]\(" # Positive lookbehind
    happy_smiley = re.sub(pattern, ")", user_input)
    print(happy_smiley)
    #else:
        #print(user_input)

happy_face(user_input)