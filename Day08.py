#!/usr/bin/env python3

print ("File I/O")
print ("""Write a script that reads a text file and counts how many lines and words are in the file""")


# Provide user's input
filename = input("Enter the name of the text file: ")

# Function to count lines and words in a file
def count_lines_and_words(filename):
    try:
        # Open the file in read mode
        with open(filename, "r") as file:
            lines = file.readlines()  
            line_count = len(lines)  
            word_count = sum(len(line.split()) for line in lines)  

        # Print the results
        print(f"Number of lines: {line_count}")
        print(f"Number of words: {word_count}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

# Main program
if __name__ == "__main__":
    count_lines_and_words(filename)








