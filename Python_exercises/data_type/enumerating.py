# How to use enumerate


list_of_days = ["monday", "tuesday", "wednesday", "thursday", "friday"]

index = 0
for index, day in enumerate(list_of_days):
    #print(day)
    index += 1
    print(f"{day.capitalize()} is day {index}")

# Another way doing it using the range

index = 0
for index in range(len(list_of_days)):
    day= list_of_days[index]
    index += 1
    print(index, day.capitalize())