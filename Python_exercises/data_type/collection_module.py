# Collection module

# Counting wit Counter from collections

from collections import Counter



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

print(counter)


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

#counter = Counter(Apple=3, Beer=1)
#print(counter)

# Available in 3.10
#print(counter.total())


# Counters can also be used with some binary operators

counter = Counter(Apple=1, Cabbage=2)
counter2 = Counter(Cabbage=1, Carrot=2)

print(counter + counter2)

print(counter - counter2)

print(counter & counter2)


#

from collections import OrderedDict
a_dict = {"name": "Mary", "age": 54}
ordered = OrderedDict(a_dict)
print(ordered)

ordered.move_to_end("age", last=False)

print(ordered)
"""


# ChainMap 
# Very similar to the update method in dictionaries

from collections import ChainMap

root = {"a":1, "b": 2}

adjust1 = {"b":3, "c":4}

chain = ChainMap(adjust1,root)
print(type(chain))

# Merging it from right to left, replacing the b value in the "left" dict

print(dict(chain))

print(chain['a'])

print(chain['b'])

print(chain['c'])

# ChainMap is more than updating, it has a memory
# It remembers which dictionaries were merged to produce the object

print(chain.maps)

# property maps has a list of input elements
# This list can be manipulated and the main object will be changed
chain.maps[0]['a'] = 100
print(chain['a'])