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
getcontext().prec = 15 # Changing precision of answer, goes to 15 decimal points

# Probably an easier way to error-handle this but it works.
startZ = False  # Can't get z without getting x first
start = False   # When user has correctly entered both x and z, start the rest

while startZ == False:
    try:
        x = float(input("Enter a number: "))
        while x < 1:
            print("Please enter a positive number!")
            x = float(input())
        startZ = True

    except ValueError:
        print("Please only enter number values, try again.")

while start == False:
    try:
        z = float(input("Sqrt guess: "))
        start = True
    except ValueError:
        print("Please only enter number values, try again.")

# Print answer using built-in math.sqrt function
# Convert to Decimal for more accuracy, also get the absolute values in case user entered negative num
# Abs function adapted from https://www.tutorialspoint.com/python/number_abs.htm
print("Math.sqrt(x): \t\t" + str(Decimal(math.sqrt(abs(x))))) # Accurate sqrt

# Convert x and z to Decimals
x = Decimal(abs(x))
z = Decimal(abs(z))

# Do the first calculation
approximate = z - ((z*z - x) / (2 * z))
difference = 1  # Init the difference in answers at 1 - if init at 0, while loop won't run
count = 1 # Calculation already done once

while difference > 0.00000000001:
    z = approximate # set new z to be last answer
    approximate = z - ((z*z - x) / (2 * z))
    difference = z - approximate  # Keep track of difference between z and approx
    count = count + 1

print("Newton's Method: \t" + str(approximate) + " (" + str(count) + " iterations)")