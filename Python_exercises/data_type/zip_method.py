# How to use the zip method
"""
x = [1,2,3]

print(max(x))


# Loop to get the max_value
max_value = 0

for number in x:
    if number > max_value:
        max_value = number
    print(max_value)
    #max(number)


y = ['a', 'b', 'c', 'd']

p = ['x', 'y', 'z', 'q']

z = zip(x,y,p)

print(z)


#d = dict(z)
#print(d)

#for i in z:
    #print(i)"""

# How to 

books = [
    {"cost": 10, "name": 'Python 2'},
    {"cost": 1, "name": 'Best tourism sites in Napoli'},
    {"cost": 5, "name": 'Basket Weaving for Pros'},
    {"cost": 8, "name": 'Java for dummies'},
]
# print(sorted(books, key=lambda book: book['cost']))

# readable!
func = lambda book: book['cost']
print(sorted(books, key=func))

func1 = lambda book: book['name']
print(sorted(books, key=func1))