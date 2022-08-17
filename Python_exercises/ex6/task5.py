# Task 5 - summing three integers

x = int(input("First number: "))
y = int(input("Second number: "))
z = int(input("Third number: "))

if x == y or y == z or x==z: # equal operator is missing and x==z
    result = 0
    print("Caluclated sum is ", result)
else:
    sum = x + y + z
    print("Caluclated sum is ", sum) 

