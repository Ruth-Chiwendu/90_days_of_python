#!/usr/bin/env python3

print ("Build a simple age checker,Ask the user for their age and tell them if their eligible for certain services.")
print ("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - -")

# Ask for users input for age
age = input("Enter Yor Age: ")

# Convert age from string to integer
age = int(age)

# Check if users is eligible for a particular service
if age >= 18:
    print ("You are eligible to vote.")
elif age >= 16:
    print ("You are allowed to attend parties, But do not take Alcohol without permission.")
elif age >= 13:
    print ("You are allowed to go for slumber parties.")
else:
    print ("You are not a teenager yet!")
