# How to do if else in python

age = int(input("Enter your age: "))

if age >= 18:
    print("You are now signed up.")
elif age < 0:
    print("You are not born yet.")
elif age > 50:
    print("You are too old to sign up.")
else:
    print("You are not 18+")
