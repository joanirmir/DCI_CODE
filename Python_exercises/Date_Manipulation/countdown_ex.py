# Create a program that takes an int as input
# - uses this int as a countdown
# - visibly counts down
# - prints begin time, end time and countdown int

# Importing the sleep function from time library

import time
import os 

integer = int(input("Enter an integer for your countdown: "))

def countdown(integer):
    
    print(f"Now the countdown begins at: {time.time()}")
    
    os.system("clear")

    for i in range(integer, 0, -1):
        time.sleep(1)
        print(i)
    
    print("The countdown is over!")

countdown(integer)