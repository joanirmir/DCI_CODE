# Task 8 - Fibonacci series

# Yor task is to write a Python program to get the Fibonacci series between 0 to 50

# Note: The Fibonacci Sequence is the series of numbers: 0,1,1,2,3,5,8,13,21,...

# Define the first two numbers and their sum

"""
a = 0
b = 1
sum = a + b
print(a)
print(b)
while b < 50:
    a, b = b, sum
    sum = a + b
    print(sum)
    if b + sum > 50:
        break
"""   

# Solutions
# In this solution the first number x = 0 is not printed

x, y = 0, 1

while y < 50:
    print(y)
    x, y = y, x+y
