#!/usr/bin/env python3

print ("DICTIONARIES and SET")
print ("""TASK:Create a program that stores user information (name, age) in a dictionary and allows the user to 
retrieve it by providing the name""")
print ("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -- - - -")

user_info = {"Name": "Ruth Chiwendu", "City": "New York", "Gender": "Female"}

#Take User's input
user_input = input("Enter a key: ")

#Search for the key in dictionary
found = False
for key, value in user_info.items():
    if user_input ==key:
        print (f"The value for '{user_input}' is: {value}")
        found = True
        break

#if the key is not found
if not found:
    print(f"Key '{user_input}' Not Available in Dictionary.")

