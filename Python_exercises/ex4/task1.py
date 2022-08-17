# Task 1

# The user has to be asked three times about two integer numbers to compare.

i = 0
while i < 3:
    print(i)
    i += 1
    number = (input("Enter first number: "))
    number2 = (input("Enter second number: "))
    if number != number2:
        print("Numbers are not equal")
    elif number < number2:
        print("Second number is greater than first number")
    elif number <= number2:
        print("Second number is greater than or equal to first number")
    elif number == number2:
        print("The numbers are equal.")
    else:
        print("Number is required")


    