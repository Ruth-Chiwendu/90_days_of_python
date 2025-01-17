#!/usr/bin/env python3
import json

print ("Working with JSON")
print ("TASK: Create a script that reads a JSON file and prints out specific values based on user input")

#open json file and read
with open ('Ruth_data.json', 'r') as file:
           data =json.load (file)

#Ask for user input
key = input ("Enter the key to fetch it's values: ")

#if key not found print

print (data.get(key, "key not found."))

