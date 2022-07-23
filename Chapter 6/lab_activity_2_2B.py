"""
    Nestor Ingles Jr
    CTI 110 001
    Lab Activity 2.2B: Working with Strings
"""

# Assigns a valut to the string we will be working on
word = input("Word to convert: ")

# This is the assigments of a negative number to represent the number
# of characters from the end of the string
count = int(input("How many letters at the end of the word should be converted? "))

# This is the first part of the string
first_str = word[0:len(word) - count]

# This is the second part of the string
second_str = word[-count:]

# Printing first part of the string + second part of the string (Formatted)
print(first_str + second_str.upper())
