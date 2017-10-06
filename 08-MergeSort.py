# 8 - Merge Lists and Sort
# Source: https://adriann.github.io/programming_problems.html
# Write a function that merges two sorted lists into a new sorted list. [1,4,6],[2,3,5] → [1,2,3,4,5,6]

list1 = []
list2 = []
newlist = []
i = 0

print("Please enter 3 numbers for each list.")

print("List 1")
while i < 3:
    try:
        listItem = float(input(str(i + 1) + ": "))
        list1.append(listItem)
        i = i + 1

    except ValueError:
        print("Please only enter number values, try again.")

print("List 2")
i = 0  # Reset i
while i < 3:
    try:
        listItem = float(input(str(i + 1) + ": "))
        list1.append(listItem)
        i = i + 1
    
    except ValueError:
        print("Please only enter number values, try again.")

newList = list1 + list2

print()
print("List 1: " + str(list1))
print("List 2: " + str(list2))
print("New List: " + str(newList))
print("Sorted List: " + str(sorted(newList))) # Adapted from https://docs.python.org/3/howto/sorting.html