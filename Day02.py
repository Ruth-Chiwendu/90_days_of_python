#!/usr/bin/env python3

print("- Create a program that takes user input for their name and age, then prints a greeting with their name and calculates the year they were born.")

print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

# Provide users input for name and age
name = input("Enter Your Name: ")
age = input ("Enter Your Age: ")

# Convert age to integer so it won't be read as a string
age =int(age)

# To calculate year of birth
current_year = 2025
year_of_birth = current_year - age

# Print a greeting with the name and year of birth
print (f"Hi {name}!!, Trust you're good. You were born in the year {year_of_birth}.")


