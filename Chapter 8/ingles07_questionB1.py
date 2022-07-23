"""
Name: Nestor Ingles Jr
Course:  CSC - 121
Assignment:  Chapter 8: Programming Project Part B
Program Name: Stop and Smell the Roses
"""
# Get input from the user
string = input("Enter string with no spaces and capitalized words: ")

# Declaring secondary string for output
sec_string = ""

# Initiating count
i = 1

# Making first character upercase
sec_string += string[0].upper()

# While loop to add spaces and
# finish reading characters as lowercase to sec_string
while i < len(string):
    if string[i].islower():
        sec_string += string[i]
    else:
        sec_string += " " + string[i].lower()
    i += 1

# Printing output
print(sec_string)
