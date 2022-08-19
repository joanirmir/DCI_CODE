# Importing libraries

import os
import time
import datetime

# Sending it later as an email

from smtplib import *
from email.mime.multipart import * #optional (advanced)
from email.mime.text import *
from email.message import *

from colorama import *
#from art import *

# Initializing colorama

init()

# Defining the date and datetime

day = (datetime.datetime.today().strftime("%d-%m-%Y %H:%M:%S"))
print(day)

# Display current journal

#with open("diary.txt", "r") as f:
    #file_contents = f.read()
#print(file_contents)

# Art gui
#print(Fore.LIGHTCYAN_EX+"")
#tprint("Awesome Journal", font="random")
#print(+Style.RESET_ALL) # To end the style

# Input of the user

new_entry = input("ENTER DIARY ENTRY HERE >>> ")

# Open the txt and create a new entry

cwd = os.getcwd()

if cwd in new_entry:
    print("")
elif new_entry != "":
    with open("diary.txt", "a") as file:
        file.write((day + " " + new_entry + "\n"))

#if new_entry == "": #if entry is not empty
    #with open("diary.txt", "a") as file:
        #file.write
#elif os.getcwd() in new_entry:
    #print("Something went wrong. Not adding.")
#else:
    #print("New entry: ")
    

