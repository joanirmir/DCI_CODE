# Importing libraries

import os
import time
import datetime


from smtplib import *
from email.mime.multipart import * #optional (advanced)
from email.mime.text import *
from email.message import *

from colorama import *
# from art import *

# Initializing colorama
init()

# Defining the date and datetime

day = (datetime.datetime.today().strftime("%d-%m-%Y %H:%M:%S"))
print(day)

# Input of the user

new_entry = input("ENTER DIARY ENTRY HERE >>>")

with open("diary.txt", "a") as file:
    file.write(day + " " + new_entry + "\n")
    

