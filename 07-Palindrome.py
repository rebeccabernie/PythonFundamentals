# 7 - Palindrome Test
# Source: https://adriann.github.io/programming_problems.html
# Write a function that tests whether a string is a palindrome.

print("Palindrome Test")

run = True

while run == True:
    word = input("Enter a word: ")
    print("Original: " + str(word))
    print("Reversed: " + str(word)[::-1])  # [ begin not specified : end not specified : steps of -1 ]
    # Reverse a string adapted from https://stackoverflow.com/questions/931092/reverse-a-string-in-python
    
    if str(word) == str(word)[::-1]: # If original is the same as the reversed
        print("This is word is a palindrome.")
        print()

    else:
        print("This is word is not a palindrome.")
        print()

    # In case user wants to test another word
    again = input("Test another word? Y/N: ")

    if again.lower() == "y":
        run = True
    elif again.lower() == "n":
        run = False
    else:
        again = input("Please enter Y/N: ")
