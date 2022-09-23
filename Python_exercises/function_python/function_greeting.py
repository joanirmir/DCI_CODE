# Greeting functions


"""def full_name(first_name="John/Jane", last_name="Doe"):
    return f"Good morning {first_name} {last_name}"

print(full_name(last_name="Peter"))"""

# How to use *args 
def full_name(*args):
    return f"{args[0]} {args[1]} {args[2]} {args[3]}"

print(full_name("Felipe", "Gonzales", "Pedro", "Alfonso II"))