# Task 1
from datetime import datetime, timedelta

current_datetime = datetime.now()

dir(current_datetime)

substracted_days = timedelta(-15)

new_date = current_datetime + substracted_days

# Convert datetime "new_date" zu 
only_date = new_date.strftime("%Y-%M-%d")

print(only_date)
print(new_date)

print(type(only_date))
print(type(new_date))