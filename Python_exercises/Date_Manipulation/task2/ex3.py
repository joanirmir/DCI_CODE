import datetime

start_date = datetime.datetime(year=2021, month=1, day=25)

new_date = start_date.strftime("%d %B, %Y")

print(start_date)
print(new_date)

print(type(start_date))

message = f"Hello Friedrich, your rent of 300€ is due on {new_date}."

print(message)


