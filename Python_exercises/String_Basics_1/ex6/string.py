#

given_string = "there was a really nice story about a man transformed to a insect named Gregor. Hey how are you"

given_string.index("H")
H = given_string[80]

given_string.index("a")
a = given_string[7]

given_string.index("l")
l = given_string[15]

given_string.index("o")
o = given_string[26]

given_string.find("Gregor")
Gregor = given_string[72:78]

Hello_Gregor = f'"{H}{a}{l}{l}{o} {Gregor}"'

print(Hello_Gregor)