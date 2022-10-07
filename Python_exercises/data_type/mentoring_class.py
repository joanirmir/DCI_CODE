# A list is a sequence

l = [2,3,4,5,6,8]

for index in range(5):
    print(index)

for index in range(5):
    l[index] = l[index] + 1

# Update the elements, combining the built-in functions range and len:

for i in range(len(l)):
    l[i] = l[i] * 2



print(l[len(l)-1])

print(l[3:5])

client_names = ['mathias', 'sarah', 'helena', 'john', 'helmut']

client_emails = ['matias@matias.de', 's.tidkw@web.de', 'helena245@.gmail.com', 'john@web.de', 'helumt346@dfa']

client_age = [39, 23, 45, 24, 58]

mathias = {}