# 6 - Largest and Smallest in a List
# Source: https://adriann.github.io/programming_problems.html
# Write a function that returns the largest and smallest elements in a list.

numbers = []
i = 0

print("Please enter 5 numbers.")

while i < 5:
    try:
        listItem = float(input(str(i + 1) + ": ")) # Get input from user
        numbers.append(listItem) # Add item to array of numbers
        i = i + 1

    except ValueError:
        print("Please only enter number values, try again.")
    

print(numbers) # Output the list

# Min and Max function adapted from https://stackoverflow.com/questions/2622994/python-finding-lowest-integer, using float in case user enters non-whole number
lowest = min(float(i) for i in numbers)
print("Lowest number: " + str(lowest))
highest = max(float(i) for i in numbers)
print("Highest number: " + str(highest))
