secret = input("secret: ")
gift_heart = input("love name: ")
birthday = input("year of birth: ")

if len(secret) >= 8:
    print(secret[::-1] + gift_heart[::-1] + birthday)
else:
    print("The secret must be at least 8 characters")

