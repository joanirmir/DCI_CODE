# Task 6 - Celsius to Fahrenheit conversion

scale_shortcut = input("Input the scale shortcut you'd like to convert (F- Fahrenheit, C - Celsius: ")
value = int(input("Input the value of temperature you'd like to convert: "))

if scale_shortcut == "C":
    print(f"The temperature in Fahrenheit is {(value*1.8)+32}")
elif scale_shortcut == "F":
    if value == int or float:
        print(f"The temperature in Celsius is {(value-32)*1.8}")
else:
    print("Check your input again")