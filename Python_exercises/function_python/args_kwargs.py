# Function (args, kwargs)

# keyword arguments are dictionaries
# args are tuple
'''def full_name(**kwargs):
    first_name = kwargs["first_name"]
    last_name = kwargs["last_name"]
    return f"{first_name} {last_name}"

# how to use it!
print(full_name(first_name='Jane', last_name='Doe'))

# how to get data from people
print(full_name(first_name=input('What is your first name?'),
                last_name=input("What is your last name? ")))


# has no input arguments

def hello():
    return "Guten Tag"

# This function has arguments
#def 


first_name = "" # global variable
last_name = "Doe"
def full_name():
    first_name = "Peer" # local variable (with local scope)
    last_name = "Hofmann"
    return f"{first_name} {last_name}"

print(full_name())

print(first_name)
print(last_name)

# With list

last_name = ["Doe"] # but if the data type is list the global changes
# pass by value (usually does not change global scoped variable)
def full_name(last_name):
    # variations
    last_name[0] = "Hoffmann"
    return last_name

full_name(last_name)
print(last_name)'''


# With dictionary

last_name = {"first_name": "John", "last_name":"Doe"}
def full_name(last_name):
    last_name[0] = "Sally"
    return last_name

# the variable without changes
print(last_name)
# executing the function and printing it with changes
print(full_name(last_name))
# the global variable is changed by the local variable
print(last_name)