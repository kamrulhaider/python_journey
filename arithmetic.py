# friends = 5

# Basic 4 operation
# friends += 1
# friends -= 2
# friends *= 5
# friends /= 2

# Exponent

# friends **= 2

# Modulus

# friends %= 2


# print(friends)


# Buil in math related function

# x = 3.14
# y = -4
# z = 5

# result = round(x)
# result = abs(y) # absolute value
# result = pow(4, 3)  # power
# result = max(x, y, z) # maximum value
# result = min(x, y, z) # minimum value

# print(result)

# math module
import math

# x = 9

# print(math.pi)
# print(math.e)
# print(math.sqrt(x))
# print(math.ceil(x))
# print(math.floor(x))


# Excercise 1: circumference of a circle

# radius = float(input("Enter a radius of a circle: "))

# circumference = 2 * math.pi * radius

# print(f"The circumference of the circle is {circumference}")

# Excercise 2: Calculation of a circle Radius

# radius = float(input("Enter a radius of a circle: "))

# area = math.pi * pow(radius, 2)

# print(f"The area of the circle is {round(area,2)}")

# Excercise 3: Calculation of hypotenuse of a triangle

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"The hypotenuse of the triangle is {c}")
