# Random Story telling

# Importing random module

import random

# Sentence_starter
sentence_starter = ["50 years ago", "In 2200", 
                    "Once upon a"]

character = [" there lived a dragon. ", " there was a cat. ", 
             " there lived a dog named Brutus. "]

time = ["One day", "One full-moon night", "On the weekend"]

story_plot = [" he was passing by", " he was eating a steak"]

place = [" in the mountains", " in the garden"]

second_character = [" he saw a man", " he was sitting in the garden"]

age = [" who seemed to be in late 50s", " who seemed very old and feeble"]

work = [" searching the ring", " digging a well on roadside"]

# Selecting an item from each list and concatenating them
story = print(random.choice(sentence_starter)+random.choice(character)+
      random.choice(time)+random.choice(story_plot)+
      random.choice(place)+random.choice(second_character)+
      random.choice(age)+random.choice(work))


print("He was approaching you. Where do you go?")
print("(1) left (2) straight (3) right")
choice = input("Choose: ")

if choice == "1":
    print("you go left and you run into a lake and died")
elif choice == "2":
    print(f"You are going to where {random.choice(character)}")
    print("(1) wait (2) run (3) attack")
    choice = input("Choose: ")
    if choice == "1":
        print("Good for you the other didn't see you.")
        print("(1) slowly go away (2) you find another path to follow (3) you got to the other one though.")
        choice = input("Choose: ")
        if choice == "1":
            print("You are reaching a clearing.")
        elif choice == "2":
            print("There you are meeting a gnome.")
            print("(1) Say hello (2) ignore (3) attack")
            choice = input("Choose: ")
            if choice == "1":
                print("The gnome is ignoring you and you go take a break.")
            elif choice == "2":
                print("The gnome gets angry and kills you.")
            elif choice == "3":
                print("You have a huge fight.")
        elif choice == "3":
            print("Nice, you found a new friend!")
    elif choice == "2":
        print("You didn't run fast enough. He followed you and you were killed.")
    elif choice == "3":
        print("Now the character is really angry.")
        print("(1) wait (2) run (3) attack")
        choice = input("Choose: ")
        if choice == "1":
            print("Sorry you were eaten.")
        elif choice == "2":
            print("Good, you could escape. Enjoy the rest of you day.")
        elif choice == "3":
            print("Good for you you have your sword with you and can kill the character.")
elif choice == "3":
    print("You go right and there is a wall.")
    print("(1) You climb over the wall (2) You destroy the wall with a hammer.")
    choice = input("Choose: ")
    if choice == "1" or choice == "2":
        print("You see a dragon who lives behind the wall.")
else:
    print("You wait")
