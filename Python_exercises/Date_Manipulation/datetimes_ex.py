# Datetime Modules (Dates and Times)

# Importing datetime

import datetime

# Use dir() to see all the classes of the library

dir(datetime)

# Use help() for more information

help(datetime.date)

# datetime.date() takes three arguments - year, month, day

gvr = datetime.date(1956, 1, 31)

# Access one argument via variable.month/ variable.day / variable.year

print(gvr)
print(gvr.month)
print(gvr.year)
print(gvr.day)

# How to use datetime.timedelta()

mill = datetime.date(2000, 1, 1)
dt = datetime.timedelta(100)

# Print the variable assigned to the date plus the variable of 100 days and gives you the exact date 100 days later

print(mill + dt)

# Day-name, Month-name Day-#, Year

print(gvr.strftime("%A, %B %d, %Y"))

# How to use the .format() module to display the format you chose

message = "GVR was born on {:%A, %B %d, %Y}."
print(message.format(gvr))

# datetime.date , datetime.time, datetime.datetime

launch_date = datetime.date(2017, 3, 30)
launch_time = datetime.time(22, 27, 0)
launch_datetime = datetime.datetime(2017, 3,30, 22, 27, 0)

print(launch_date)
print(launch_time)
print(launch_datetime)

# You can access the hours, the minutes, the seconds of .time

print(launch_time.hour)
print(launch_time.minute)
print(launch_time.second)

# Access current datetime:
# - Module: datetime
# - Class: datetime
# - Method: today()

# Call the module datetime, then the class datetime and then the method today()

now = datetime.datetime.today()
print(now)
print(now.microsecond)

# Convert Strings to Datetimes

moon_landing = "7/20/1969"

# Convert string to datetime: - Module: datetime - Class: datetime - Method: strptime()

moon_landing_datetime = datetime.datetime.strptime(moon_landing, "%m/%d/%Y")

print(moon_landing_datetime)

print(type(moon_landing_datetime)) # class 'datetime.datetime'

