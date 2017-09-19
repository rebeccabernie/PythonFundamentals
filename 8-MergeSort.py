# 8 - Merge Lists and Sort
# Source: https://adriann.github.io/programming_problems.html
# Write a function that merges two sorted lists into a new sorted list. [1,4,6],[2,3,5] → [1,2,3,4,5,6]

list1 = []
list2 = []
newlist = []

print("Please enter 3 numbers for each list.")

print("List 1")
for i in range (0,3):
    listItem = float(input(str(i + 1) + ": "))
    list1.append(listItem)

print("List 2")
for i in range (0,3):
    listItem = float(input(str(i + 1) + ": "))
    list2.append(listItem)

newList = list1 + list2

print()
print("List 1: " + str(list1))
print("List 2: " + str(list2))
print("New List: " + str(newList))
print("Sorted List: " + str(sorted(newList))) # Adapted from https://docs.python.org/3/howto/sorting.html