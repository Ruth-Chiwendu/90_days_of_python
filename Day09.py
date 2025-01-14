#!/usr/bin/env python3

print("Error handling")

print("""TASK- Create a program that takes user input for a number and catches errors if the user inputs something
invalid (non-integer)""")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

#Ask for user input
user_input=input("Enter a number: ")
try:
    #convert user input to integer
    number=int(user_input)
    print(f"You entered a number: {number}")
except ValueError:

    print("Invalid input!!Enter a number.")

