# Task 7 - pattern

#j = "*"
#print(" *\n",2*j+"\n", 3*j+"\n", 4*j+"\n", 5*j+"\n", 4*j+"\n", 3*j+"\n", 2*j+"\n", j+"\n")

#print("*", 2* "*", 3* "*", 4* "*", sep="\n")


# Using a for loop to create the pattern

# end= argument

n = 5
for i in range(n):
    for j in range(i+1):
        print("*", end="") 
    print()

for o in range(n-1, 0, -1):
    for k in range(o):
        print("*", end="")
    print()

# *
# **

# Making a function

#def star pattern (n):
