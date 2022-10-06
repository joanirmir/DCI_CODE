# any() & all()


# end of the month, you want to see who has paid their subscription

"""netflix_subscribers = [
    {"name": "Fausto", "paid": False},
    {"name": "Jacque", "paid": False},
    {"name": "Pasco", "paid": True},
    {"name": "Wessam", "paid": False},
    {"name": "Emily", "paid": True},
]

paid =[]
for subscriber in netflix_subscribers:
    if subscriber['paid']:
        paid.append(subscriber)
# logic @ boolean 
print(len(paid), len(netflix_subscribers))
have_all_paid = len(paid) == len(netflix_subscribers)



# map function to capitalize the first string

names = ['jacque doe', 'peer doe', 'mirjam doe', 'shaban doe']

all_names_capitalize = map(lambda name: name.capitalize(), names)
print(list(all_names_capitalize))

# How to capitalize both strings

names = ['jacque doe', 'peer doe', 'mirjam doe', 'shaban doe']

# Gives capital letter to every word
all_names_capitalize = map(lambda name: name.title(), names)
print(list(all_names_capitalize))

names = ['reiner', 'peter', 'john']
# filter out names that end with er # -classical / traditional

names = filter(lambda name: not name.endswith('er'), names)
print(list(names))"""

# How to remove a value from a dictionary using filter and lambda

names = [{'name': 'jacque doe'}, {'name': 'peer doe'}, {'name': 'mirjam doe'}, {'name': 'shaban doe'}]

names = filter(lambda names: not names['name'].startswith('jacque'), names)
print(list(names))