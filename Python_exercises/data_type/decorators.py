"""def outer():
    def inner():
        print("Hello, I am inner")
    return inner

o = outer()  
print(o)

def outer(name):
    def inner():
        print(f"Hello {name}, I am inner")
    return inner # have not executed it!!
    
# division case
def check_divisor(func):
    def inner(a, b):
        if b == 0:
            print("You cannot divide by 0")
            return
        return func(a,b)
    return inner

def divide(a, b):    
    return a / b

divide = check_divisor(divide)
print(divide(4, 2))
print(divide(4, 0))

@check_divisor
def divide(a, b):
    return a/ b
print(divide(4,2))
print(divide(4,0))
"""



# practical use-cases
# API - a way of accessing data from on location (URL (website))
# Application Programming Interface


"""def make_title(func): # we expect the function to return a string
    def inner():
        return func().title()

    return inner        

@make_title
def greetings():
    return "hi there


#print(greetings())
def make_title(func): # we expect the function to return a string
    def inner(name):
        print('name', name, 'in make_title')
        return func(name).title()

    return inner  

def add_mr_ms(func): # we expect the function to return a string
    def inner(name):
        return func(f"Mr/Ms. {name}")
    return inner        

@add_mr_ms
@make_title
def greetings(name):
    return name

print(greetings('faust doe'))

#def capitalize(name):
    #return f'{name.title()}'

"""


def make_title_in_word(function):
    def inner(name):
        return function(name).title()
    return inner

def add_ms(function):
    def inner(name):
        return function(f'Ms {name}')
    return inner

@make_title_in_word
@add_ms
def greet_some_humans(name):
    return "Good morning " + name

print(greet_some_humans('wojciech doe'))