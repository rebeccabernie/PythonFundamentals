# 3 - FizzBuzz
# Source: http://wiki.c2.com/?FizzBuzzTest
# Write a program that prints the numbers from 1 to 100, except for the following conditions. For multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

# Start the range at 1, end at 100 (set to 101 to include 100)
for i in range(1,101):
    # Check first if number is a multiple of both 3 and 5
    # Modulo: e.g. 9 % 3 = 0 -> modulo is 0 (i.e. you can divide number by 3 with remainder 0)
    if (i % 3 == 0 and i % 5 == 0):
        print ("FizzBuzz")
    # Otherwise check if multiple of 3
    elif i % 3 == 0:
        print ("Fizz")
    # Or multiple of 5
    elif i % 5 == 0:
        print ("Buzz")
    # Else just print the number
    else:
        print (i)
