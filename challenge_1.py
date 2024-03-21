"""This program takes side of a triangle form the user and prints out the
area of the triangle"""

import math

# Ask the user to enter the lengths of all three sides of a triangle.
# Calculate the area of the triangle.
# Print out the area.


def validate(user_input):
    while True:
        if user_input.isdigit():
            return int(user_input)
        else:
            user_input = input("Invalid number. Please try again: ")


a = validate(input("Please enter the first side: "))
b = validate(input("Please enter the second side: "))
c = validate(input("Please enter the third side: "))

s = (a + b + c) / 2
area = math.sqrt(s*((s-a)*(s-b)*(s-c)))

print(f"The area of the triangle is: {area}")
