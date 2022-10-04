
"""name = ('Mirjam', 'Lingoda')
other_name = ('Peer', 'Hofman')

# tuples (are immutable)

print(name + other_name)
print(name)

# tuples are sequence data types

numbers = (1,2, 3,4,5,6,7,8,9)
print(numbers[1:4]) # slicing means you have a start and a stop but without including without - slicing operations

# inbuilt "len" function/method
print(len(numbers))

#dir(numbers)
#help(dir(numbers))

# negative indexing
print(numbers[-2])

# max
print(max(numbers))

# quotient and remainder
# 4/ 2 = 2; 5 / 3 --> 1 (reminder: 2)
# I want to return both the quotient and remainder

def quotient_remainder(x, y):
    quotient = x // y # integer division (floor)
    remainder = x % y # modulo operation
    return (quotient, remainder)

# assigment
(q, r) = quotient_remainder(5, 3)
print(q)
print(r)

'''Design a function that takes in a gender and a firstname and last name. 
If the gender is "male", return a greeting (Good morning Mr. <first name>) and a fullname.
If the gender is "female", return a greeting (Good morning Ms. <first name>) and a'''

# tuple return mutiple outcomes

def greeting_fullname(first_name, last_name, gender):
    greeting = ""
    if gender == 'male':
        greeting = f"Good morning Mr. {first_name}"
    else:
        greeting = f"Good morning Ms. {first_name}"
    
    return (greeting, full_name)

print(greeting_fullname('Mirjam', 'Langer', 'female'))

# Iteration? Going through each element of a collection
sizes = ("S", "L", "XL", "X", "L", "XL", "X")
# for loops? - slices?
for s in sizes[::-1]: # Reverse
    print(s)


# What is a list?
# Ordered sequence of information that are accessible by an index
# We denote by the use of square brackets-> [ ]
# list contain elements that can be mixed data types (not common/ not encouraged) and homogenous data types
# Lists are mutable! (Changeable)

sizes = ['l', 'xl', 'xxl']
print(len(sizes))

#access items in a list
print(sizes[0])

i = 100
print(sizes[i-99]) # expressions!!

sizes[0] = 'L'
sizes.insert(100, '5')
print(sizes)

# for loop iteration

# design a while loop

sizes = ['l', 'xl', 'xxl', 's', 'x']

s = 0 # counter variable
while s < len(sizes): # Condition has to be true
    s += 1
    print(sizes[s])"""

"""count = 0
while count < 5:
    count = count + 1
    print("Hello Geek")"""

# Exercise
# To get a total, we have a function that looks like this, rewrite (refactor) the function to use a while loop


"""def total_list(lst):
    total = 0
    for item in lst:
        total += item
    return total
# test case
print(total_list([1,2,3]))   # answer is 6


def total_list(lst):
    t = 0 # Variable to add every item by index of a list
    total = 0 # Variable to store the sum of the item of the list
    while t < len(lst): # If the index of the item is smaller than the length of the list the loop will iterate
        total += lst[t] # Add the indexes of the list together in the total variable
        t += 1          # Define the step of t to iterate through 
    return total


# test case
print(total_list([1,2,3]))
print(total_list([3,3,3]))

# for loop
fruits = ["orange", "apple", "cherry"]
string = " "
for e in fruits:
    string += e + " "
print(string)

# while loop
f = 0
while f < len(fruits):


# while loop example with weight

weight = ['10kg', '20kg', '30kg']

w = 0
while w < len(weight):
    print(f"You are {weight[w]}")
    w += 1

    weight = ['10kg', '20kg', '30kg']

colors = ['red','green', 'yellow']
counter = 0
while counter < len(colors):
    print(f"I love {colors[counter]}")
    counter += 1"""

# Operations on lists
# Add things to list
#lst = []
#lst.append

list_a.pop()