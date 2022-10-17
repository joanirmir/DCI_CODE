# We checked the passwords and user is authenticated

# And we will authorize the user ...

authorized = False

# Create a decorator is_authorized that receives a function
def is_authorized(f):
    def decorated_function(*args, **kwargs):
        if is_authorized:
            f(*args, **kwargs)
        else:
            print('Not authorized!')
    return decorated_function

def append_details(f):
    def decorated_function(*args, **kwargs):
        details = '-----\n'
        details += f(*args, **kwargs)
        details += '\nversion: v1.0\n'
        details += '-----\n'
        return details
    return decorated_function





@is_authorized
def list_users():
    print('Mathias\nMary\nSarah')

@is_authorized
def app_version():
    print('v1.0')

@append_details
def user_data():
    return 'name: Matias'


list_users()
app_version()
print(user_data())