# 9 - Newton's Method for Square Roots
# Source: https://tour.golang.org/flowcontrol/8
# Implement the square root function using Newton's method. In this case, Newton's method is to approximate sqrt(x) by picking a starting point z and then repeating z_next = z - ((z*z - x) / (2 * z))
# To begin with, just repeat that calculation 10 times and see how close you get to the answer for various values (1, 2, 3, ...). Next, change the loop condition to stop once the value has stopped changing (or only changes by a very small delta). How close are you to the math.sqrt value?

# Logic
# x is the number you want to find the sqrt of
# z is a guess at what the sqrt is?

# Decimal functionality adapted from https://docs.python.org/2/library/decimal.html and https://stackoverflow.com/questions/35619309/how-to-increase-the-precision-of-float-values-to-more-than-10-in-python

import math
from decimal import *
getcontext().prec = 15

x = Decimal(input("Enter a number: "))
z = Decimal(input("Sqrt guess: "))

print("Math.sqrt(x): \t\t" + str(Decimal(math.sqrt(x)))) # Accurate sqrt

approximate = z - ((z*z - x) / (2 * z))
difference = 1
count = 1 # Calculation done once

while difference > 0.00000000001:
    z = approximate
    approximate = z - ((z*z - x) / (2 * z))
    difference = z - approximate
    count = count + 1

print("Newton's Method: \t" + str(approximate) + " (" + str(count) + " iterations)")