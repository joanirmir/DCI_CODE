# Write a function to make two names titelized e.g. title_name(name1, name2)

def title(name1, name2):
    return name1.title(), name2.title()

def joining_names(list):
    return ''.join(list)

print(joining_names(["name1", "name2", "name3"]))