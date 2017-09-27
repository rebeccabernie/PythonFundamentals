# 4 - Factorial Digit Sum
# Write a function that calculates the sum of the digits of the factorial of a number. n! means n x (n − 1) ... x 3 x 2 x 1. For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800, and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27. Find the sum of the digits in the number 100!

print("Factorial & Digit Sum Calculator")
f = input("Enter a number: ")
n = 1 # start at 1 for each calculation

for i in range(1, int(f) + 1): # start at 1, go to number + 1 (will stop at number)
    n = n * i             # let answer = previous number times the current value of i, e.g 2 x 3, that answer x 4, so on

def digitSum(n):
    currentPos = 0
    digits = []
    digitSum = 0
    answer = str(n) # Stringify answer to make it loopable

    # Loop through answer, add digits to list
    for digit in answer:
        currentNum = str(answer[currentPos]) # Current number = what's at the current position
        digits.append(currentNum) # Add the number to the digit list
        currentPos = currentPos + 1 # Go forward a position

    # Loop through list of digits to get sum
    for num in digits:
        digitSum = digitSum + int(num)

    return digitSum


print(str(f) + "! = " + str(n))
print("The sum of the digits of " + str(f) + "! is " + str(digitSum(n)))