import datetime

start_date = datetime.datetime(year=2021, month=1, day=25)

print(start_date)

print(type(start_date))

message = f("Hello Friedrich, your rent of 300€ is due on {datetime.strptime(start_date, "%M %A, %Y")}")


user_input = input("Enter ")

start_date = datetime(year=2020, month=1, day=1)