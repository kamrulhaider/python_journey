# Logical Oparators: Logical Oparators are used to evaluate multiple logical conditon expressions.
# in pythons operators are and, or, not

# Example: We will allow the boy to play outside if his age is more than 30 years and is fit to play outside.

# age = 35
# isFitToPlay = True

# if age > 30 and isFitToPlay:
#     print("You are allowed to play outside.")
#     print("Let's go!")
# else:
#     print("You are not allowed to play outside.")

# Example: We will allow the boy to play outside if his age is more than 30 years or if he is a student.

# age = 35
# isStudent = True

# if age > 30 or isStudent:
#     print("You are allowed to play outside.")
#     print("Let's go!")
# else:
#     print("You are not allowed to play outside.")

# Example: We will allow the boy to play outside if there is no rainfall and he is a student

isStudent = True
isRaining = False

if isStudent and not isRaining:
    print("You are allowed to play outside.")
    print("Let's go!")
else:
    print("You are not allowed to play outside.")
