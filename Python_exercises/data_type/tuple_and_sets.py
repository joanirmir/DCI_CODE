# Tuple
"""
name = "Hello"

print(tuple(name))

x = ()
print(type(x))

# Not a tuple, type integer with just one item
y = (3)
print(type(y))

x = (3, )
print(type(x))

something = ('a', 'b', 'c', 'c', 'c', 'c')

something.count('c')
something[0] = 'x' # Tuples can't be change - immutable

x = ([], )
x[0].append('Shaban') # adding to a data structure that can change like a list
print(x)

y = ('string', )
y[0] = 'hahaha' # Gives an error, tuples cannot be mutated


# Converting from a tuple to a list
# pass the tuple to the list constructor

x = list(x)
print(type(x))


# Sets

food = {"Salmon", "Codd", "Salmon"}
print(food)

name = "Lucas Schwertel"
set(name)

# counter for the names? dict?

name = name.lower()

counter = {}

for letter in name: 
    counter[letter] = counter.get(letter, 0) + 1

print(counter)

# Tip: creating a default key/value pair: counts.setdefault(key, value)

name = "lucas schwertel"
set(name)

counter = {}

for key in set(name):
    counter.setdefault(key, name.count(key))

print(counter)


name = "lucas schwertel"
set(name)
counter = "Lucas Schwertel"

for char in name.lower():
    counter[char] += counter[char] +1

print(counter)
word = "this word has many words with duplicates"
counts = {}
for char in set(word.lower()):
    counts.setdefault(char, 0)
    counts[char]= counts[char] +1

print(counts)"""


# Set operations

fruits = {"Pear", "Mango", "Apple", "Strawberry"}

smoothie = {"Mango", "Orange", "Pear"}

#fruits.intersection(smoothie)

"""fruits.difference(smoothie)

# symmetric difference (XOR) - set A and B without intersection

fruits.symmetric_difference(smoothie)

fruits.intersection_update(smoothie)
print(fruits, 'after')

smoothie.intersection_update(fruits)
print(fruits, "next")

print(fruits, smoothie)
fruits.symmetric_difference_update(smoothie)
print(fruits, smoothie)"""

fruits.union(smoothie)
