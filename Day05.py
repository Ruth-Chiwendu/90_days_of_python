#!/usr/bin/env python3
print ("FUNCTIONS")
print ("This covers -Types of function")
print ("How to define 'def' and 'call' functions")
print ("Covered -Arguments, -Return values -Variable Scope")
print ("-----TASK: Write a function that takes a number as input and returns the factorial of that number.")
#use 'def' to define the variable

def factorial(num):

    # Initialize factorial to 1
    result = 1

    # Loop from 1 to num (inclusive) to calculate the factorial
    for i in range(1, num + 1):
        result *= i

    # Print the result
    print(f"The factorial of the number {num} is {result}")

# Get user input and convert it to an integer
user_input = int(input("Enter a number: "))

# Call the factorial function with the user input
factorial(user_input)

