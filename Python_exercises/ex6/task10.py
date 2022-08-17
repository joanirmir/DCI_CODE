# Task 10 - divisible number

x = int(input("First number: "))
y = int(input("Second number: "))

if x % y == 0:
    print("First number is divisible by second number, result = ", float(x//y))
elif y % x == 0:
    print("Second number is divisible by first number, result= ", float(y//x))
else:
    print("Numbers are no-divisiable!")

#