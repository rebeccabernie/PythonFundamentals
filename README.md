# Problem Sheet 1 - Python Fundamentals

> Module: Emerging Technologies / 4th Year  
> Lecturer: Dr Ian McLoughlin  
> [Original Problem Sheet](https://github.com/emerging-technologies/emerging-technologies.github.io/blob/master/problems/python-fundamentals.md)

*Need to add some error handling.*

## Goals

The aim of these problems is to give you a good knowledge of basic Python. The problems are good for either learning Python from scratch or refreshing your memory of the language. They cover a variety of variable types, calculations, loops, user input, and in-built functions, among other things.

## Exercises

**1. Hello World**  
A standard "Hello World" program.

**2. Current Time**  
Prints the current time to the screen.

**3. FizzBuzz**  
This program outputs all numbers 1 - 100 inclusive. If a number is divisible by 3, "Fizz" is printed instead of the number. The same goes for multiples of 5, except "Buzz" is printed. If a number is a multiple of both 3 and 5, the output is "FizzBuzz". For example:  
```
1         
2         
Fizz      
4         
Buzz      
Fizz      
7         
8         
Fizz      
Buzz      
11        
Fizz      
13        
14        
FizzBuzz  
```

**4. Factorial**  
The user enters a number. The factorial of that number is calculated by multiplying it by every number preceding it and the result is printed to the screen. For example, `5! = 5 x 4 x 3 x 2 x 1 = 120`. The program also calculates the sum of the digits in the answer, i.e. `120 = 1 + 2 + 0 = 3`.

**5. Guessing Game**  
The program generates a random number for the user to guess. The program tells the user if their guess was too high or too low, and tells them how many tries it took them when they get the number right. The program does not count multiple guesses of the same number. Below is an example of one game, notice how 33 was guessed twice but only counted as a try once.  
```
Guess a number between 1 and 50.  
Your guess: 25                    
Too low, try again.               
38                                
Too high, try again.              
33                                
Too low, try again.               
33                                
Too low, try again.               
35                                
Too low, try again.               
36                                
You're right!                     
It took you 5 tries.              
```

**6. Smallest and Largest in a List**  
The user enters a list of 5 numbers, and the program calculates and prints the smallest and largest numbers in the list.

**7. Palindrome Test**  
The user enters a word (or sentence), and the program tests whether the string is a palindrome (i.e. the original and reverse of the word are spelled the same).

**8. Merge Two Lists and Sort**  
The user enters two lists containing three numbers each. The program merges the two lists into one, and sorts the new list from lowest to highest.

**9. Newton's Square Root Method**  
The user enters a number and their guess for the square root of that number. The program uses Newton's method to calculate the square root using the user's guess (z), the original number(x), and the new approximate(the equation result from the last iteration of the loop):

```
newApproximate = z - ((z* - x) / (2 * z))
```

The program stops calculating a new approximate when the change in results between loops becomes less than 0.00000000001.

**10. Reverse a String**  
The user enters a word or sentence. The program reverses the string using both the easy, built in `str(word)[::-1]` function, and a written function that loops through the string to reverse it manually. Both results are the same.