# Factorial method

"""def  factorial(n):
    # base case
    if n == 0:
        return 1
    else:
        # expensive (your computer might crash)
        return n * factorial(n - 1)

print(factorial(3))

for i in range(1000):
    print(factorial(i), f'i->{i}')  # i -> 997



# Rewrite this to use a recursive style
# Have a base case, where to stop



def get_sum(lst):
    total = 0
    for i in lst:
        total += i
    return total

print(get_sum(lst))

lst = [1,2,3,4,5,6,7,8,9]

def recursive_style(lst):
    result = lst[0]+[1]
    print(result)
    delete = lst.pop(0,1)
    print(delete)

    return result + recursive_style(lst[i])

print(recursive_style(lst))


def sum(lst):
    if not lst:
        return 0
    else:
        first = lst.pop(0)
        return first + sum(lst)

print(sum([1,3,5,9]))

# Sometimes you have to write a function in a function

def outter_function():
    def inner_function():
        return "I am an inner function"

    return inner_function()"""

# Think python - example
# 5.8 Recursion
# It is also legal for a function to call itself

# Example one:
def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)

print(countdown(3))
    