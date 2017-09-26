# 6 - Largest and Smallest in a List
# Source: https://adriann.github.io/programming_problems.html
# Write a function that returns the largest and smallest elements in a list.

numbers = []

print("Please enter 5 numbers.")

for i in range (0,5):
    listItem = float(input(str(i + 1) + ": "))
    numbers.append(listItem)

print(numbers) # Output the list

# Min and Max function adapted from https://stackoverflow.com/questions/2622994/python-finding-lowest-integer, using float in case user enters non-whole number
lowest = min(float(i) for i in numbers)
print("Lowest number: " + str(lowest))
highest = max(float(i) for i in numbers)
print("Highest number: " + str(highest))
