"""
Name: Nestor Ingles Jr
Course:  CSC - 121
Assignment:  Chapter 8: Programming Project 2
Program Name: Capitalize Strings
"""

# Defining main function
def main():
    # Get input from user
    original_string = input("Enter sentence to be capitalized: ")
    # Split string input into a list
    string_list = original_string.split(".")
    # Declare string for output
    concat_string = ""

    # For loop to loop through list
    for i in string_list:
        if i[0] != " ":
            concat_string += (i[0].upper() + i[1:] + ".")
        else:
            concat_string += (i[0] + i[1].upper() + i[2:] + ".")
    print(concat_string[:-1])

# Call main
main()
