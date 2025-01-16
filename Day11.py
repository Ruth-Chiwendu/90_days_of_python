#!/usr/bin/env python3

print ("Regular Expression")
print ("Build a program that validates email addresses using regular expressions")
print ("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

#Ask for user's input
user_email=input("Please Enter a valid Email Address: ")

import re

def validate_email(email):
    # Define the regex pattern for email validation
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    # Use the re.match function to check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False

    # Validate the email address
if validate_email(user_email):
    print(f"{user_email} is valid!!")
else:
    print(f"{user_email} is invalid. Please enter a valid email")

