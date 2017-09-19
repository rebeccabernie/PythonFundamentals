# 5 - Guessing game
# Source: https://adriann.github.io/programming_problems.html
# Write a guessing game where the user must guess a secret number. After every guess the program tells the user whether their number was too large or too small. At the end the number of tries needed should be printed. It counts only as one try if they input the same number multiple times consecutively.

from random import randint

print("Guess a number between 1 and 50.")
secretNum = randint(0,50)
# Generate random int adapted from https://stackoverflow.com/questions/3996904/generate-random-integers-between-0-and-9


# Take input from the user and convert to int
userGuess = int(input("Your guess: "))

# While guess is wrong, take more inputs
while userGuess != secretNum:
    if userGuess < secretNum:
        print("Too low, try again.")
        userGuess = int(input())

    elif userGuess > secretNum:
        print("Too high, try again.")
        userGuess = int(input())

# If guess is right, tell user
if userGuess == secretNum:
    print("You're right!")