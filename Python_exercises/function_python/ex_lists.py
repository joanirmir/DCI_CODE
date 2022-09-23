# Data type lists

from hashlib import new


names = ["Victor", "Peter", "Mary", "John", "Badara", "Peer"]
print(names)

# Using an index, replace "Peer" with "Malcom X"

names[-1] = "Malcom X"
print(names)

# Add two names to the list of names

names.append("Waheed")
names.append("Bahaa")
names.append("Felipe")
print(names)

# How to add while using a loop
#new_list = []

#for i in names:
    #new_list.append(i) 

# Adding two lists together and creating a new list

#new_list = ["a", "b"]
#super_new_list = names + new_list
#print(super_new_list)

# Another way with using extend and updating the first list
#names.extend(new_list)
#print(names)


# Experiment with the methods in a list using dir(names)

#dir(names)
#help(dir())

# Removing

# names.pop()

# Reverse the elements

names.reverse()
print(names)

