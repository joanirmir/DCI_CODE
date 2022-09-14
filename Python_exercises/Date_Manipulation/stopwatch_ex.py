# Create a program that saves current time and prints it
# - saves another time moment and prints it
# - prints the time that has passed in between

# Importing the date from the library datetime

import time

first_time = (time.time())
print(time.ctime(first_time))

second_time = (time.time())
print(time.ctime(second_time))

passed_time = second_time - first_time

print(f"Seconds that did pass: {round(passed_time,2)}")

#converted_time = time.ctime(passed_time)

#print(converted_time)

"""

import timeit
start = timeit.timeit()
print("hello")
end = timeit.timeit()
print(end -start)
'''


