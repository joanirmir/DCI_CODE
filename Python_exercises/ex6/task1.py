# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn

# Task 1 - fix the FizzBuzz

three_mul = "fizz" # bug: misses an '
five_mul = "buzz"
num1 = 3
num2 = 5 #5, not 4
max_num = 100

for i in range(1,max_num):
    # % or modulo division gives you the remainder

    if i%num1 == 0 and i%num2 == 0: #has to be the first if because of two conditions have to be met
        print(i, three_mul+five_mul)
    elif i%num1 == 0: # "=" was missing
        print(i, three_mul + five_mul)
    elif i%num2 == 0:
        print(i, five_mul) #intendation