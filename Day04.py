#!/usr/bin/env python3

print ("LOOPS")
#Loops are used to repeat a block of code as a condition is met.
#Types of Loops- For Loops & While Loops

print ("Task- Create a simple countdown program that counts down from 10 to 1 using a while loop.")
print ("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -- - - ")

#prints a countdown from 10 to 1
i = 10
while i> 0:
    print(i)
    i -= 1
    
#Note: print (i) prints the current value of i and i -= 1 decreases the count by 1
print ("Countdown Completed!!!")
print ("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

print ("THE USE OF 'for' LOOPS-- to iterate a list")

#The use of For loops
fruits=["Apples", "Banana", "Kiwi", "Berries", "Lemon", "Coconut"]
for fruit in fruits:
    print (fruit)