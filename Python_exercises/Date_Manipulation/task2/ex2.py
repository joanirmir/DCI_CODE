# Task 2

from datetime import datetime, timedelta

current_datetime = datetime.now()

new_time = current_datetime + timedelta(days=7)

print(new_time)

only_date = strftime(new_time, %Y-%M-%d)