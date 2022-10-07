# Counting 

"""fridge = [
    "Apple", "Apple", "Cabbage",
    "Steak", "Cheese", "Apple",
    "Carrot", "Carrot", "Iogurt",
    "Beer"
]

counter = {}
for ingredient in fridge:
    if ingredient not in counter:
        counter[ingredient] = 0
    counter[ingredient] += 1

print(counter)"""

from collections import Counter

fridge = [
    "Apple", "Apple", "Cabbage",
    "Steak", "Cheese", "Apple",
    "Carrot", "Carrot", "Iogurt",
    "Beer"
]

# counter is an instance of the constructor with the data of fridge

counter = Counter(fridge) # pay attention to the capital letter of the constructor
print(counter)

# A counter can also be created empty or passing items as keyword arguments:

counter = Counter(Apple=3, Beer=1)
print(counter)