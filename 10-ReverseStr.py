# 10 - Reverse String
# Write a function to reverse a string.

word = input("Enter a word: ")

# Easy Way
print("Original: " + str(word))
print("Easy Reverse: " + str(word)[::-1])

# Function
def reverse(word):
    reversedWord = []
    currentPos = len(word) - 1 # Start at the last letter (5 letters = 0 - 4)
    endAt = 0 # End at the first letter

    for letter in word:
        currentLetter = str(word[currentPos]) # Current letter is what's at the current position
        reversedWord.append(currentLetter) # Add the letter to the reversed word list
        currentPos = currentPos - 1 # Go back a position 

    return ''.join(reversedWord) # Adapted from https://stackoverflow.com/questions/5618878/how-to-convert-list-to-string

print("Function Reverse: " + str(reverse(word)))