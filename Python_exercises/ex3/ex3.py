# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn

# Task 1 - basic math operations


#from tracemalloc import start


#number1 = 0
#umber2 = 0
#number3 = 0

for i in (range(3)):
    i = int(input("Enter a number: "))
    if i%2 == 0:
        print("The number is even")
    else:
        print("The number is odd")


# Task 2 - printing numbers with range() function

# First we create the variable number that contains the user input

#number = input("Enter a number here: ")

#start_number = int(input("Enter starting number: "))
#stop_number = int(input("Enter stopping number: "))
#step_number = int(input("Enter step number: "))

#for i in range(start_number, stop_number, step_number):
#   print(i)


# We use for loop to define the range for the numbers 1,2,3
for number in range(1,4):
    if number == 1:
#Number 1 asks the user for another number:
        n1 = print(input("Enter another number: "))
        for i in range(n1):
            print(n1)
    elif number == 2:
#Number 2 asks the user for two numbers:
        n2 = print(input("Enter two numbers: "))
        n3 = print(input("Enter your second number: "))
        for i in range(n2,n3):
            print(n2,n3)
# Number 3 asks the user for three numbers:
    else:
        n4 = print(input("Enter your first number: "))
        n5 = print(input("Enter your second number: "))
        n6 = print(input("Enter your third number: "))
        for i in range(n4,n5,n6):
            print(n4,n5,n6)



# Task 3 - finding divisors of a number

# The program should print all the divisors of a number.
# First we need the input from the user.

i = 0

user_number = input("Enter a number: ")
for i in range(2, user_number+1):
    if user_number%i == 0:
        print(i)


# Task 4 - check prime number

# The program should check if input number is a prime number

user_number = int(input("Enter a number: "))
if user_number>1: 
    for i in range(2, user_number):
        if (user_number%i) == 0:
            print(user_number, "is not a prime number")
            break
    else:
        print(user_number, "is a prime number")

# Task 5 - FizzBuzz

# Write a program that prints the numbers from 1 to 100

for i in range(1, 101):
    if i %3 == 0:
        print("Fizz")
    if i %5 == 0:
        print("Buzz")
    if i %3 == 0 and i %5 == 0:
        print("FizzBuzz")
    else:
        print(i)


"""

# Task 6 - divisible numbers

# Write a program to print all the numbers between 1000 and 2000 which are divisible by 7 but are not a multiple of 5.

for i in range(1000, 2001):
    if i %7 == 0 and i %5 != 0:
        print(i)