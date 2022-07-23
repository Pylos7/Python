"""
Name: Nestor Ingles Jr
Course:  CSC - 121
Assignment:  Chapter 7: Programming Project 1
"""
# Defining main function
def main():

    # Open BoyNames and GirlNames files for reading
    infileb = open("BoyNames.txt", "r")
    infileg = open("GirlNames.txt", "r")

    # Read the contents of the file into a list
    boynames = infileb.readlines()
    girlnames = infileg.readlines()

    # Close the files
    infileb.close()
    infileg.close()

    # Strip the \n from each element in boynames
    index = 0
    while index < len(boynames):
        boynames[index] = boynames[index].rstrip("\n")
        index += 1

    # Strip the \n from each element in boynames
    index = 0
    while index < len(girlnames):
        girlnames[index] = girlnames[index].rstrip("\n")
        index += 1

    # Asking for boy names, girl names, or both
    name_sex = input("Enter \'boy\', \'girl\', or \'both\':")

    # If statement that will run dependingon the name type
    if name_sex == "boy":
        # Getting a name
        name = input("Enter a boy\'s name:")

        # If statement with print statement saying whether the name is popular or not
        if search(boynames, name) == True:
            print(name + " was a popular boys\'s name between 2000 and 2009.")
        else:
            print(name + " was not a popular boy\'s name between 2000 and 2009.")

    # Elif statement that will run dependingon the name type
    elif name_sex == "girl":
        # Getting a name
        name = input("Enter a girl's name:")

        # If statement with print statement saying whether the name is popular or not
        if search(girlnames, name) == True:
            print(name + " was a popular girl\'s name between 2000 and 2009.")
        else:
            print(name + " was not a popular girl\'s name between 2000 and 2009.")

    # Elif statement with print statement saying whether the name is popular or not
    elif name_sex == "both":
        # Getting a name
        name = input("Enter a name:")

        # If statement with print statement saying whether the name is popular or not
        if search(girlnames, name) == True:
            print(name + " was a popular girl\'s name between 2000 and 2009.")
        else:
            print(name + " was not a popular girl\'s name between 2000 and 2009.")

        if search(boynames, name) == True:
            print(name + " was a popular boy\'s name between 2000 and 2009.")
        else:
            print(name + " was not a popular boy\'s name between 2000 and 2009.")
    else:
        # Error Message
        print("Please enter \"girl\", \"boy\", or \"both\"")

        # Calling main in case inputs are wrong
        main()

# Defining search function
def search(list, namematch):

    for i in range(len(list)):
        if list[i] == namematch:
            return True
    return False

# Calling main
main()
