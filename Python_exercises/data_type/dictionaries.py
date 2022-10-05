## What are dictionaries?

fruit_colors = {
    "apple": "red",
    "berries": "blue"
}

"""# to avoid a crash, use a method like .get()
print(fruit_colors.get("X", None))

# .get() method takes an optional extra argument that defines the default value
print(fruit_colors.get("x", "Yellow"))


# You can iterate over dictionaries

for key in fruit_colors:
    print(f"The color of {key} is {fruit_colors[key]}")

# Different methods
# To loop over the keys

print(fruit_colors.keys())
for k in fruit_colors.keys():
    print(k)

# To loop over the values

print(fruit_colors.values())
for v in fruit_colors.values():
    print(v)"""

'''#print(fruit_colors.items()) #returns a list with tuples that have a key and value in it
for a_tuple in fruit_colors.items():
    print(a_tuple)
    # "unpacking" the tuple, extracting information
    x, y = a_tuple
    print(x)
    print(y)
    print("=" * 10)

for x, y in fruit_colors.items():
    print(x)
    print(y)
    print("=" * 10)'''

# Puzzle

d = {
    "soccer": "played with a ball",
    "paddle": "Fake tennis",
    "poker": "played in vegas"
}

# delete a key that ends with "er" by creating a copy of the dictionary with .copy()

for k in d.copy():
    if k.endswith('er'):
        del d[k]
print(d)