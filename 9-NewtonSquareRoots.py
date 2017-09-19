# 9 - Newton's Method for Square Roots
# Source: https://tour.golang.org/flowcontrol/8
# Implement the square root function using Newton's method. In this case, Newton's method is to approximate sqrt(x) by picking a starting point z and then repeating z_next = z - ((z*z - x) / (2 * z))
# To begin with, just repeat that calculation 10 times and see how close you get to the answer for various values (1, 2, 3, ...). Next, change the loop condition to stop once the value has stopped changing (or only changes by a very small delta). How close are you to the math.sqrt value?

# Logic
# x is the number you want to find the sqrt of
# z is a guess at what the sqrt is?

import math

x = float(input("Enter a number: "))
z = float(input("Sqrt guess: "))

print("Math.sqrt(x): \t" + str(math.sqrt(x))) # Accurate sqrt

approximate = z - ((z*z - x) / (2 * z))

for i in range (0,3):
    z = approximate
    approximate = z - ((z*z - x) / (2 * z))

print("Approximate: \t" + str(approximate))