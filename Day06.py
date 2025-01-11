#!/usr/bin/env python3

print("LIST and TURPLES")
print("- - - -TASK:Create a program that takes a list of numbers and prints the sum and average.")
print("- - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
print("use the following numbers - 10, 20, 30, 40, 50")

#Define the function
def calculate_sum_and_average(numbers):

#Calculate the sum of the numbers
    total_sum=sum(numbers)

#calculate the average of the numbers
    average=total_sum / len(numbers)

    return total_sum,average

#list the numbers
numbers =[10, 20, 30, 40, 50]
total_sum, average = calculate_sum_and_average(numbers)

#Print the result
print(f"Sum of numbers: {total_sum}")
print(f"Average of numbers: {average}")



