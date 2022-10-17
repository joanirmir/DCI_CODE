def annoying_decorator(f):
    def decorated_function(*args, **kwargs):
        print('I will not do what you want!')

    return decorated_function

@annoying_decorator
def greeting(name):
    print(f'Hi {name}')

greeting('matias')

@annoying_decorator
def sum(x, y):
    return x + y

print(sum(3,4))