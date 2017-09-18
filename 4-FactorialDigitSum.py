# 4 - Factorial Digit Sum
# Write a function that calculates the sum of the digits of the factorial of a number. n! means n x (n − 1) ... x 3 x 2 x 1. For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800, and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27. Find the sum of the digits in the number 100!

f = 10 # Factorial number = 10
n = 1 # start at 1

for i in range(1, f + 1): # start at 1, go to number + 1
    n = n * i             # let previous number times the current value of i

print(n)