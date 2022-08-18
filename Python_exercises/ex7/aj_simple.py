import os
import time
import datetime

from colorama import *
from art import *

# Initialize color effects 
init()

# Default blank spaces
clear = "\033[2J\033[1;1f" 
space = "\n" * 20

# Time variables
# today = datetime.date.today().strftime("%d-%m-%Y")
now = str(datetime.datetime.today().strftime("%H:%M:%S %d-%m-%Y"))

here = os.getcwd() # Current working directory

# Defining AJ function
print(clear)
print(space)
#print(""


print("")
print(now+Style.RESET_ALL)
newentry = input(">>> ")
if os.path.exists('log.txt') == False:
    log = open('log.txt', 'w')
    log.write(now + " " + newentry)
    log.close()
elif os.path.exists('log.txt') == True:
    log = open('log.txt', 'a')
    log.write("\n" + now + " " + newentry)
    log.close()
print(clear)
print(space)
print(Fore.LIGHTGREEN_EX+"")
tprint("     AJ ENTRY SAVED!", font="cyber")
print(""+Style.RESET_ALL)
time.sleep(0.5)
os._exit(0)