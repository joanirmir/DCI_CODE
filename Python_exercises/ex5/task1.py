# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn

# Task 1 - calculate sum

# We have to use three inputs to get three integers

number1 = int(input("First number: "))
number2 = int(input("Second number: "))
number3 = int(input("Third number: "))

# We need the sum of all three numbers

result = number1 + number2 + number3
print(result)

# If all three numbers are equal we triple the sum

if number1 == number2 == number3:
    print(f"The triple sum is: {result*3}")
else:
    print(result)

