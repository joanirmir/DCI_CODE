# Create a program that takes an int as input
# - uses this int as a countdown
# - visibly counts down
# - prints begin time, end time and countdown int

# Importing the sleep function from time library

from time import sleep

integer = int(input("Enter an integer for your countdown: "))

def countdown(integer):
    
    print("Now the countdown begins!")
    
    for i in range(integer, 0, -1):
        sleep(1)
        print(i)
    
    print("The countdown is over!")

countdown(integer)