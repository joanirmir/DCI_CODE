# Task 2 - convertion month name to a number of days

# User should be prompted to enter name of the month and the output should be the number of days in given month.

months = ["January", "February", "March", "April", "May", "June", "July", 
          "August", "September", "October", "November", "December"]


user = input("Input the name of Month: ")
if user == months[0]:
    print(user,": Number of days: 31 days")
elif user == months[1]:
    print("Number of days: 28 days")
elif user == months[2]:
    print("Number of days: 31 days")
elif user == months[3]:
    print("Number of days: 30 days")
elif user == months[4]:
    print("Number of days: 31 days")
elif user == months[5]:
    print("Number of days: 31 days")
elif user == months[6]:
    print("Number of days: 30 days")
elif user == months[6]:
    print("Number of days: 30 days")
elif user == months[7]:
    print("Number of days: 30 days")
elif user == months[8]:
    print("Number of days: 31 days")
elif user == months[9]:
    print("Number of days: 30 days")
elif user == months[10]:
    print("Number of days: 31 days")
elif user == months[11]:
    print("Number of days: 30 days")
else:
    print("Check for type error")





