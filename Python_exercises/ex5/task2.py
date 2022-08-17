# Task 2 - get the difference

number1 = int(input("First number: "))
number2 = int(input("Second number: "))

if number1 > number2:
    print(f"The result of calculation is: {(number1-number2)*2}")
else:
    print(f"The result of calculation is: {abs(number1-number2)}")


