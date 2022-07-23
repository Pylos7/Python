x = 35.2
y = 24
print(type(x), type(y))
print(x, 'converts to integer', int(x))
print(y, 'converts to float', float(y))
resStr = str(x + y)
charList = list('abracadabra')
print(resStr, charList)
listStr = str(['a', 'c', 'e'])
print(type(listStr), listStr)

ANum = ord('A')
BNum = ord('B')
ZNum = ord('Z')
spaceNum = ord(' ')
print(ANum, BNum, ZNum, spaceNum)
print( chr(100), chr(111), chr(103))


# Block Comment
print("Hello World!")

print("Hello World!")   # Inline Comment

"""
Documentation Comment - Docstrings are often used to document modules, functions, and class definitions.
"""
print("Hello World!")


name, hobbies = input("What is your name? "), input("What are your hobbies? ")

print("Your name is", name, "and your hobbies are", hobbies)

# Nestor Ingles Jr
# CSC 121 001

bank_balance = float(b("Enter current bank balance:"))
interest_rate = float(input("Enter interest rate:"))
months_passed = int(input("Enter the ammount of time that passes:"))
print(bank_balance * (1 + interest_rate) ** months_passed)



# Revel wanted functions but did not ask for them so I did not know what to do untill I saw the answer.

def savings(present, interest, time):
    return present * (1 + interest)**time

def main():
    present = float(input('Enter current bank balance:'))
    interest = float(input('Enter interest rate:'))
    time = float(input('Enter the amount of time that passes:'))
    print(savings(present, interest, time))

main()


# Nestor Ingles Jr
# CTI 110 001
# Lab Activity 2.1B: Using Different Arithmetic Operators
days_driving = int(input("Days you have been driving:"))
years = int(days_driving / 365)
weeks = int((days_driving % 365)/7)
days = int(days_driving % 365) % 7
print("You have been driving for:\nYears:", 
years, "\nWeeks:", weeks, "\nDays:", days)


# Python3 code to convert given
# number of days in terms of
# Years, Weeks and Days
 
DAYS_IN_WEEK = 7
 
# Function to find
# year, week, days
def find( number_of_days ):
 
    # Assume that years is
    # of 365 days
    year = int(number_of_days / 365)
    week = int((number_of_days % 365) /
                DAYS_IN_WEEK)
    days = (number_of_days % 365) % DAYS_IN_WEEK
     
    print("years = ",year,
          "\nweeks = ",week,
          "\ndays = ",days)
     
# Driver Code
number_of_days = 200
find(number_of_days)
 
# This code contributed
#by "Sharad_Bhardwaj"



<string>.<method>(<inputs>)

Method	Description
lower/upper	Converts to lower or upper case
strip	Removes given chars from ends of string
split	Breaks a string into substrings
join	Builds one string from a list of strings
count	Count occurrences of substring
find	Find the position where a substring occurs
isalpha	Check if all characters are alphabetic
isdigit	Check if all characters are digits


Escape Sequence	Definition
\newline	Backlash and newline ignored
\\	Backlash (\)
\’	Single quote (‘)
\”	Double quote (“)
\a	ASCII Bell (BEL)
\b	ASCII Backspace (BS)
\f	ASCII Formfeed (FF)
\n	ASCII Linefeed (LF)
\r	ASCII Carriage Return (CR)
\t	ASCII Horizontal Tab (TAB)
\v	ASCII Vertical Tab (VT)
\ooo	Character with octal value ooo
\xhh	Character with hex value hh

# Nestor Ingles Jr
# CTI 110 001
# Practice Exercise 2.2: Using Escape Sequences

sentence = input("Sentence: ")
sentence = sentence.replace(" ", "\n")
print(sentence, "\a")




# Index slicing
s1 = 'abracadabra'
print(s1[4:7])
print(s1[:4])
print(s1[7:])
print(s1[::3])
print(s1[::-1])






# How to open a file
file_variable = open("filename", "mode")

"""
    r - Open a file for reading only. The file cannot be changed or written to.
    
    w - Open a file for writing. If the file already exists, erase its contents. If the file does not exist, create it.
    
    a - Open a file to be written to. All data written to the file will be appended to its end. If the file does not exist, create it.
    
"""
# Oppening a file in windows
test_file = open(r'C:\Users\Blake\temp\test.txt', 'w')

# Calling the write method
file_variable.write(string)

# Example 1
customer_file.write('Charles Pace')

# Example 2
name = 'Charles Pace'
customer_file.write(name)

# Closing an output file forces any unsaved data tha remains in the memory buffer to be written to the file. Ex. the following closes the file that is associated with customer_file.
customer_file.close()

# This program reads and displays the contents of the philosopers.txt file.
def main():
    # Open a file named philosophers.txt
    infile = open("philosophers.txt", "r")
    
    # Read the file's contents.
    file_contents = infile.read()
    
    # Close the file
    infile.close()
    
    # Print the data that was read into memory
    print(file_contents)
    
# Call the main function
main()


# The readline method is used to read a line from a file including its \n.

# This program reads the contents ofthe pholisophers.txt file one line at a time.
def main():
    # Open a file named philosophers.txt.
    inline = open("philosophers.txt", "r")
    
    # Read 3 lines from the file.
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    
    # Close the file.
    infile.close()
    
    # Print the data that was read into memory
    print(line1)
    print(line2)
    print(line3)

# Call the main function.
main()

# A read position is mantained when oppeninf files with "r" the read position is changed everytime readline is used.


# Appending to a file
myfile = open("friends.txt", "a")
myfile.write("Matt\n")
myfile.write("Chris\n")
mtfile.write("Suze\n")
myfile.close()


# Writing and reading numeric data
# This program demostrates how numbers must be converted to strings before they are written to a text file.
def main():
    # Open a filefor writing
    outfile = open("numbers.txt", "w")
    
    # Get three numbers from the user
    num1 = int(input("Enter a number: ")
    num2 = int(input("Enter another number: ")
    num3 = int(input("Enter another number: ")
    
    # Write the numbers to the file
    outfile.write(str(num1) + "\n")
    outfile.write(str(num2) + "\n")
    outfile.write(str(num3) + "\n")
    
    # Close the file
    outfile.close()
    print("Date written to numbers.txt")

# Call the main function
main()

# A better way of reading strings and coverting them at the same time is as follows

infile = open("numbers.txt", "r")
value = int(infile.readline())
infile.close()



# Using loops to proccess files
# Open a file
myfile = open("numbers.txt", "w")

# Write 100 random numbers to the file
for count in range(100):
    number = random.randint(1,100)
    myfile.write(str(number) + "\n")

# Close the file
myfile.close()
print("Done")




# Reading multiple values from file
# Open a file
myfile = open("numbers.txt", "r")

# Read each line in the file and display it
for line in myfile:
    print(line)

# Close the file
myfile.close()



# To strip new line character from the output
print(line, end="")


# How to determine if you are at the end of the file
# Open a file
myfile = open("numbers.txt", "r")

# Read the first line from the file (Priming Read)
line = myfile.readline()

# Continue proccessing the file
while line != "":
    print(line, end="")
    line = myfile.readline()

# Close the file
myfile.close()





# Recording sales ammounts

# This program prompts the user for sales ammounts and writes those ammounts to the sales.txt file

def main():
    # Get the number of days
    num_days = int(input("For how many days do you have sales? "))
    
    # Open a file named sales.txt
    sales_file = open("sales.txt", "w")
    
    # Get the ammount of sales for each day and write it to a file
    for count in range(1, num_days + 1):
        # Get sales for a day
        sales = float(input("Enter the sales for day #" + str(count) + ": "))
        
        # Write the sales ammount to the file
        sales_file.write(str(sales) + "\n")
    
    # Close the file
    sales_file.close()
    print("Data written to sales.txt")
    
# Call the main function
main()




# Format ammount
print(format(ammount, ".2f")




# My try at Q1
numbers_file = open('numbers.txt', 'r')

line = numbers_file.readline()
if line.len() = 0:
    line = '0'
while line != '':
    if line.len() = 0:
        line = '0'
    sum += int(line)
    line = numbers_file.readline()
    
numbers_file.close()


# The answer 

numfile = open("numbers.txt","r");
sum = 0
number = numfile.readline()
while number != "":
    sum += int(number)
    number = numfile.readline()
numfile.close()

# Conclusion - I forgot to initiate the SUM variable 


# Question 2 - making a copy of all the lines in one file into another file.

myfile = open('data1.txt', 'r')
d2file = open('data2.txt', 'w')
line = myfile.readline()
while line != "":
    d2file.write(line)
    line = myfile.readline()

# Close the file
myfile.close()







data = open('data.txt', 'r')

dataplus = open('dataplus.txt', 'w')
dataminus = open('dataminus.txt', 'w')
zeros = open('zeros.txt', 'w')

line = data.readline()

count = 0
while line != "":
    if int(line) > 0:
        dataplus.write(line)
    elif int(line) < 0:
        dataminus.write(line)
    else:
        count+=1
    line = data.readline()
zeros.write(str(count))

dataplus.close()
dataminus.close()
zeros.close()


# Program 6-13 shows a simple example of how employee records can be written to a file
# save_emp_records.py

# This program gets employee data from the user and saves it as records in the employee.txt file

def main():
    # Get the number of employee records to create
    num_emps = int(input('How many employee records do you want to create? '))
    
    # Open a file for writing
    emp_file = open('employees.txt', 'w')
    
    # Get each employees data and write it to the file
    for count in range(1, num_emp + 1):
        # Get the data for an employee
        print('Enter data for employee #' , count, sep='')
        name = input('Name: ')
        id_num = input('ID Number: ')
        dept = input('Department: ')
        
        # Write the data as a record to the file
        emp_file.write(name + '\n')
        emp_file.write(id_num + '\n')
        emp_file.write(dept + '\n')
        
        # Display a blank line
        print()
    
    # Close the file
    emp_file.close()
    print('Employee records written to employees.txt')

# Call the main function
main()




# read_emp_records.py
# This program displays the records that are
# in the employees.txt file.

def main():
    # Open the employees.txt file.
    emp_file = open('employees.txt', 'r')

    # Read the first line from the file, which is
    # the name field of the first record.
    name = emp_file.readline()

    # If a field was read, continue processing.
    while name != '':
        # Read the ID number field.
        id_num = emp_file.readline()

        # Read the department field.
        dept = emp_file.readline()

        # Strip the newlines from the fields.
        name = name.rstrip('\n')
        id_num = id_num.rstrip('\n')
        dept = dept.rstrip('\n')

        # Display the record.
        print('Name:', name)
        print('ID:', id_num)
        print('Dept:', dept)
        print()

        # Read the name field of the next record.
        name = emp_file.readline()

    # Close the file.
    emp_file.close()

# Call the main function.
main()





# add_coffee_record.py

# This program adds coffee inventory records to
# the coffee.txt file.

def main():
    # Create a variable to control the loop.
    another = 'y'

    # Open the coffee.txt file in append mode.
    coffee_file = open('coffee.txt', 'a')

    # Add records to the file.
    while another == 'y' or another == 'Y':
        # Get the coffee record data.
        print('Enter the following coffee data:')
        descr = input('Description: ')
        qty = int(input('Quantity (in pounds): '))

        # Append the data to the file.
        coffee_file.write(descr + '\n')
        coffee_file.write(str(qty) + '\n')

        # Determine whether the user wants to add
        # another record to the file.
        print('Do you want to add another record?')
        another = input('Y = yes, anything else = no: ')

    # Close the file.
    coffee_file.close()
    print('Data appended to coffee.txt.')

# Call the main function.
main()




# show_coffee_records.py
# This program displays the records in the
# coffee.txt file.

def main():
    # Open the coffee.txt file.
    coffee_file = open('coffee.txt', 'r')

    # Read the first record's description field.
    descr = coffee_file.readline()

    # Read the rest of the file.
    while descr != '':
        # Read the quantity field.
        qty = float(coffee_file.readline())

        # Strip the \n from the description.
        descr = descr.rstrip('\n')

        # Display the record.
        print('Description:', descr)
        print('Quantity:', qty)

        # Read the next description.
        descr = coffee_file.readline()

    # Close the file.
    coffee_file.close()

# Call the main function.
main()





# search_coffee_records.py
# This program allows the user to search the
# coffee.txt file for records matching a
# description.

def main():
    # Create a bool variable to use as a flag.
    found = False

    # Get the search value.
    search = input('Enter a description to search for: ')

    # Open the coffee.txt file.
    coffee_file = open('coffee.txt', 'r')

    # Read the first record's description field.
    descr = coffee_file.readline()

    # Read the rest of the file.
    while descr != '':
        # Read the quantity field.
        qty = float(coffee_file.readline())

        # Strip the \n from the description.
        descr = descr.rstrip('\n')

        # Determine whether this record matches
        # the search value.
        if descr == search:
            # Display the record.
            print('Description:', descr)
            print('Quantity:', qty)
            print()
            # Set the found flag to True.
            found = True

        # Read the next description.
        descr = coffee_file.readline()

    # Close the file.
    coffee_file.close()

    # If the search value was not found in the file
    # display a message.
    if not found:
    print('That item was not found in the file.')

# Call the main function.
main()


# modify_coffee_records.py
# This program allows the user to modify the quantity
# in a record in the coffee.txt file.

import os # Needed for the remove and rename functions

def main():
    # Create a bool variable to use as a flag.
    found = False

    # Get the search value and the new quantity.
    search = input('Enter a description to search for: ')
    new_qty = int(input('Enter the new quantity: '))

    # Open the original coffee.txt file.
    coffee_file = open('coffee.txt', 'r')

    # Open the temporary file.
    temp_file = open('temp.txt', 'w')

    # Read the first record's description field.
    descr = coffee_file.readline()

        # Read the rest of the file.
        while descr != '':
            # Read the quantity field.
            qty = float(coffee_file.readline())

            # Strip the \n from the description.
            descr = descr.rstrip('\n')

            # Write either this record to the temporary file,
            # or the new record if this is the one that is
            # to be modified.
            if descr == search:
                # Write the modified record to the temp file.
                temp_file.write(descr + '\n')
                temp_file.write(str(new_qty) + '\n')

                # Set the found flag to True.
                found = True
            else:
                # Write the original record to the temp file.
                temp_file.write(descr + '\n')
                temp_file.write(str(qty) + '\n')

        # Read the next description.
        descr = coffee_file.readline()

    # Close the coffee file and the temporary file.
    coffee_file.close()
    temp_file.close()

    # Delete the original coffee.txt file.
    os.remove('coffee.txt')

    # Rename the temporary file.
    os.rename('temp.txt', 'coffee.txt')

    # If the search value was not found in the file
    # display a message.
    if found:
        print('The file has been updated.')
    else:
        print('That item was not found in the file.')

# Call the main function.
main()




# delete_coffee_record.py
# This program allows the user to delete
# a record in the coffee.txt file.

import os # Needed for the remove and rename functions

def main():
    # Create a bool variable to use as a flag.
    found = False

    # Get the coffee to delete.
    search = input('Which coffee do you want to delete? ')

    # Open the original coffee.txt file.
    coffee_file = open('coffee.txt', 'r')

    # Open the temporary file.
    temp_file = open('temp.txt', 'w')

    # Read the first record's description field.
    descr = coffee_file.readline()

    # Read the rest of the file.
    while descr != '':
        # Read the quantity field.
        qty = float(coffee_file.readline())

        # Strip the \n from the description.
        descr = descr.rstrip('\n')

        # If this is not the record to delete, then
        # write it to the temporary file.
        if descr != search:
            # Write the record to the temp file.
            temp_file.write(descr + '\n')
            temp_file.write(str(qty) + '\n')
        else:
            # Set the found flag to True.
            found = True

        # Read the next description.
        descr = coffee_file.readline()

    # Close the coffee file and the temporary file.
    coffee_file.close()
    temp_file.close()

    # Delete the original coffee.txt file.
    os.remove('coffee.txt')

    # Rename the temporary file.
    os.rename('temp.txt', 'coffee.txt')

    # If the search value was not found in the file
    # display a message.
    if found:
        print('The file has been updated.')
    else:
        print('That item was not found in the file.')

# Call the main function.
main()





# Exception Handeling

try:
    # Try suite
    statement
    statement
    etc.
except ExceptionName: # except clause
    # Handler
    statement
    statement
    etc.
except IOError:
    statement
    statement
    etc.
except ValueError as err:
    print(err)
    statement
    etc.
except Exception as err: # assigns error message to err
    print(err)  # prints err
except:
    print('An error of some sort occurred')
else:
    # else suite
    statement
    statement
    etc.
finally: # will allways excecute and is intended to clean up or close files or resources


# for loop adding line values
for line in infile:
    ammount = float(line)
    total += ammount


# CTI 110 001
# if else statement example

# Write your code here
release_year = '1991'
answer = input('When was Python first released? ')

if answer == release_year:
    print('Congratulations! That is correct.')
elif answer > release_year:
    print('No, that\'s too late')
elif answer < release_year:
    print('No, that\'s too early')

print('Bye!')



# Lesson 3.3 - The While Statement

while condition:
    # Run this code while condition is true
    # Replace the "condition" above with an actual condition
    # This code keeps running as long as the condition evaluates to true
else:
    # Run the code in here once the condition is no longer true
    # This code only runs one time unlike the code in the while block
    
    
    
# This program gueses the number you pick
import random
userNum = int(input("Enter a number between 1 and 10: "))
print("Trying to guess your number...")
myGuess = random.randint(1, 10)
while myGuess != userNum:
    print("I guessed", myGuess, "...trying again")
    myGuess = random.randint(1, 10)
print("I guessed it! Your number was", myGuess)


# When to use a while loop
The while loop is used in the following cases:

When we must wait for a condition to be satisfied before continuing execution

When a user’s input is required—as seen in Practice Exercise 3.3B.


"""

Name: Nestor Ingles Jr
Course:  CSC-110

Assignment:  Practice Exercise 3.3A: Using the while Statement

"""

# set the starting value
current = 1
# Set the end value
end = 10

# While the current number is less than or equal to end number
while current <= end:
    # Print the current number
    print(current)
    # Increase current number by one
    current += 1
else:
    """
    Once while condition is no longer true run this code once
    """
    print("You have reached the end")
    
    
"""
Name: Nestor Ingles Jr
Course:  CSC-110
Assignment:  Practice Exercise 3.3B: Using while to Keep a Program Running
"""

# Correct answer to the question to be asked
release_year = "1991"
# Condition to check to see if we should break out of the while statement
correct = False

# This while loop willrun until the provided answer is correct
while not correct:
    # Assign user guess to answer through input
    answer = input('When was Python first released? ')
    # If statement checking if answer is right or not
    if answer == release_year:
        print('Congratulations! That is correct.')
        # Sets correct boolean to True for correct answer was provided
        correct = True
    else:
        print("No, that\'s not it. Try again\n")

# Bye message after/outside while loop
print('Bye!')


"""
Name: Nestor Ingles Jr
Course:  CSC-110
Assignment:  Lab Activity 3.3: Working with the while Statement
"""

# Defining main function
def main():
    # Getting user name from default input
    name = input("Enter your name: ")
    # Setting the password
    password = "Pas$Word"
    # Creating the boolean to control the while loop
    correct = False

    # While loop running as the bollean value of correct remains False
    while not correct:
        # Capture user password guess into guess variable from default input
        guess = input("Password: ")

        # If statement testing guess against password
        if guess == password:
            # Print login welcome message
            print("Welcome back, " + name)
            # Set corect boolean to True to allow while loop to end
            correct = True
        else:
            # Print incorrect password message
            print("Incorrect password, try again...")
    

# Calling main function
main()



"""
Iterables include some of the following:

    Strings
    Lists
    Dictionaries
    Files
"""

# "Iterable" can be anything that can be looped over e.g. a list
# "Member" is a single constituent of the iterable e.g. an entry in a list

for member in iterable:
    # Execute this code for each constituent member of the iterable
    pass





#The for Loop: Looping over Sequences
for x in ['bat', 'hat', 'rat']:
    print(x)

sum = 0
for z in (6, 1, 2, 9, 3):
    print(sum)
    sum = sum + z

for c in "rocket":
    print(c.upper())




# For loop with else statement
# Create a list with numbers 1 through 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Loop through the list of numbers
for num in numbers:
    # Calculate the square of numbers
    square = num * num
    # Print out a string showing the number and its calculated square
    print(num , "squared is", num)
#the else block will be executed exactly once the loop goes through all the members of the iterable without breaking
else:
    print("The last number was", num)




"""
Name: Nestor Ingles Jr
Course:  CSC-110
Assignment:  Practice Exercise 3.6: Using the for Loop
"""

# Initialize numbers to a list of integers from 1 to 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Loop to go through members in numbers list
for num in numbers:
    # Calculate the square and assign the value to variable square
    square = num * num
    # Printing number and its square
    print(num, " squared is ", square)
    
    
    
    
    
Lesson 3.7
The range Function
Python’s range function is a built-in function that generates a list of numbers. This list is mostly used to iterate over using a for loop.

# Syntax
range([start], stop, [step])

Here is a breakdown of what each parameter does:

start: This is the starting number of the sequence.

stop: This means generate numbers up to but not including this number.

step: This is the difference between each number in the sequence.

As a general rule, when a parameter is enclosed in square brackets [] in the function definition, it means that that particular parameter is optional when you are calling the function.

This means that the only required parameter when calling the range function is the stop parameter, and the default call to the function can have just that one parameter.


>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


What if we wanted to create a list from 1 to 10? 
>>> list(range(1, 11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


list of all even numbers between 2 and 20 inclusive
>>> list(range(2, 21, 2))
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]




for num in range(1, 11):
    print(num, " squared is ", num * num)

# Top is a rewrite of bottom

# Initialize numbers to a list of integers from 1 to 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Loop to go through members in numbers list
for num in numbers:
    # Calculate the square and assign the value to variable square
    square = num * num
    # Printing number and its square
    print(num, " squared is ", square)
    
    
    
    
# Range function examples
r1 = range(4)
print(r1, list(r1))
for i in r1:
    print(i)

r2 = range(10, 20)
print(type(r2))
print(list(r2))

for x in range(2, 24, 2):
    print(x)
    
    
    
    
    
    
    
# Lists
# You can use a statement such as the following to convert the range function's itrable object into a list

numbers = list(range(5))
[0, 1, 2, 3, 4]
nembers = list(range(1, 10, 2))
[1, 3, 5, 7, 9]

# The repetition operator
list * n

>>> numbers = [0] * 5
>>> print(numbers)
[0, 0, 0, 0, 0]
>>>

>>> numbers = [1, 2, 3] * 3
>>> print(numbers)
[1, 2, 3, 1, 2, 3, 1, 2, 3]

# You cannot create traditional arrays in Python because lists serve
# the same purpose and provide many more built in capabilities.

# Iterating over a list with the for loop

numbers = [99, 100, 101, 102]
for n in numbers:
    print(n)

99
100
101
102

# Indexing
index = 0
while index <4:
    print(my_list[index])
    index += 1

# Negative indexes
my_list = [10, 20, 30, 40]
print(my_list[-1], my_list[-2], my_list[-3], my_list[my_list[-4])
40 30 20 10

# An IndexError exception will be raised if you use an invalid index with a list

# The len function
# Return the length of a sequence

my_list = [10, 20, 30, 40]
size = len(my_list)
4

# You can use the len function to prevent an IndexError exception when iterating over a list with a loop.

my_list = [10, 20, 30, 40]
index = 0
while index < len(my_list):
    print(my_list[index]
    index += 1


# Lists are mutable
numbers[0] = 99


# Sales List Example
# The NUM_DAYS constant holds the number of
# days that we will gather sales data for.
NUM_DAYS = 5

def main():
# Create a list to hold the sales
# for each day.
sales = [0] * NUM_DAYS

# Create a variable to hold an index.
index = 0

print('Enter the sales for each day.')

# Get the sales for each day.
while index < NUM_DAYS:
print('Day #', index + 1, ': ', sep='', end='')
sales[index] = float(input())
index += 1

# Display the values entered.
print('Here are the values you entered:')
for value in sales:
print(value)

# Call the main function.
main()



# Concatenating Lists
list1 = [1, 2, 3, 4]
lsit2 = [5, 6, 7, 8]
list3 = list1 + list2
ptint(list3)
[1, 2, 3, 4, 5, 6, 7, 8]


# Keep inmind that you only cancatenate lists with other lists



# List slicing
print(names[0:3]
print(names[2:4]
print(names[:4]
print(leters[0:7:2]
print(letters[::3])
list_name[start_index : end_index : step]


# Finding items in lists with the "in" operator
# You can search for an itmes in a list with the "in" operator
 
# The expression returns true if the item is found onthe list or false otherwise
item in list

if search in prod_nums:
    print(search, 'was found in the list.')
else:
    print(search, 'was not found in the list.')


if search not in prod_nums:
    print(search, "was not found")
else:
    print(search, "was found!")


if member_id in current_members:
    is_a_member = True
else:
    is_a_member = False


# List Methods and Usefull Built-in Functions

append(item)    -   Adds item to the end of list
index(item)     -   Returns the index of the first element whose value is equal to item. A ValueError exception id raised if item is not found on the list
insert(index, item) -   Inserts item into the list at the specefied index.
sort()  -   Sorts the items in the list so they appear in accending order
remove(item)    -   Removes the first occurrance of the item from the list. A ValueError exception is raised if item is not found in the list
reverse()   -   Reverses the order of the items in the list



name_list = []
# Append the name to the list.
name_list.append(name)

# Add another one?
print('Do you want to add another name?')
again = input('y = yes, anything else = no: ') 
print()


# The index method

# This program demonstrates how to get the
# index of an item in a list and then replace
# that item with a new item.

def main():
# Create a list with some items.
food = ['Pizza', 'Burgers', 'Chips']

# Display the list.
print('Here are the items in the food list:')
print(food)

# Get the item to change.
item = input('Which item should I change? ')

try:
# Get the item's index in the list.
item_index = food.index(item)

# Get the value to replace it with.
new_item = input('Enter the new value: ')

# Replace the old item with the new item.
food[item_index] = new_item

# Display the list.
print('Here is the revised list:')
print(food)
except ValueError:
print('That item was not found in the list.')

# Call the main function.
main()



# The insert method
# This program demonstrates the insert method.

def main():
# Create a list with some names.
names = ['James', 'Kathryn', 'Bill']

# Display the list.
print('The list before the insert:')
print(names)

# Insert a new name at element 0.
names.insert(0, 'Joe')

# Display the list again.
print('The list after the insert:')
print(names)

# Call the main function.
main()



# The sort method
my_list.sort()

# The remove method
food.remove(item)

# The reverse method
my_list.reverse()




# The del Statement
# Used to remove item from list with an index no matter of what there is at that index. Ex.

del my_list[3]

# The min and max functions
# Built in functions to get the maximum or numimum value in a sequence Ex.

max(my_list)



# Copying Lists

new_list = []
for i in lst1:
    if i in lst2:
        new_list.append(i)
print(new_list)

# OR

list1 = [1, 2, 3, 4]

list2 = [] + List1

# Using list elements in a math expression

# This program calculates the gross pay for
# each of Megan's baristas.

# NUM_EMPLOYEES is used as a constant for the
# size of the list.
NUM_EMPLOYEES = 6

def main():
# Create a list to hold employee hours.
hours = [0] * NUM_EMPLOYEES

# Get each employee's hours worked.
for index in range(NUM_EMPLOYEES):
    print('Enter the hours worked by employee ', \
          index + 1, ': ', sep='', end='')
    hours[index] = float(input())

# Get the hourly pay rate.
pay_rate = float(input('Enter the hourly pay rate: '))

# Display each employee's gross pay.
for index in range(NUM_EMPLOYEES):
    gross_pay = hours[index] * pay_rate
    print('Gross pay for employee ', index + 1, ': $', \
          format(gross_pay, ',.2f'), sep='')

# Call the main function.
main()



# Totaling the values in a list

# This program calculates the total of the values
# in a list.

def main():
# Create a list.
numbers = [2, 4, 6, 8, 10]

# Create a variable to use as an accumulator.
total = 0

# Calculate the total of the list elements.
for value in numbers:
    total += value

# Display the total of the list elements.
print('The total of the elements is', total)

# Call the main function.
main()


# Averaging the values in a list

# This program calculates the average of the values
# in a list.

def main():
# Create a list.
scores = [2.5, 7.3, 6.5, 4.0, 5.2]

# Create a variable to use as an accumulator.
total = 0.0

# Calculate the total of the list elements.
for value in scores:
    total += value

# Calculate the average of the elements.
average = total / len(scores)

# Display the average of the list elements.
print('The average of the elements is', average)

# Call the main function.
main()



# Passing a list as an argument to a function

# This program uses a function to calculate the
# total of the values in a list.

def main():
    # Create a list.
    numbers = [2, 4, 6, 8, 10]

    # Display the total of the list elements.
    print('The total is', get_total(numbers))

# The get_total function accepts a list as an
# argument returns the total of the values in
# the list.
def get_total(value_list):
    # Create a variable to use as an accumulator.
    total = 0

    # Calculate the total of the list elements.
    for num in value_list:
        total += num

    # Return the total.
    return total

# Call the main function.
main()




# Returning a list from a function

# This program uses a function to create a list.
# The function returns a reference to the list.

def main():
    # Get a list with values stored in it.
    numbers = get_values()

    # Display the values in the list.
    print('The numbers in the list are:')
    print(numbers)

# The get_values function gets a series of numbers
# from the user and stores them in a list. The
# function returns a reference to the list.
def get_values():
    # Create an empty list.
    values = []

    # Create a variable to control the loop.
    again = 'Y'

    # Get values from the user and add them to
    # the list.
    while again.upper() == 'Y':
        # Get a number and add it to the list.
        num = int(input('Enter a number: '))
        values.append(num)

        # Want to do this again?
        print('Do you want to add another number?')
        again = input('y = yes, anything else = no: ')
        print()

    # Return the list.
    return values

# Call the main function.
main()



# Processing a list - Droppint the lowest test score and getting average

# This program gets a series of test scores and
# calculates the average of the scores with the
# lowest score dropped.

def main():
    # Get the test scores from the user.
    scores = get_scores()

    # Get the total of the test scores.
    total = get_total(scores)

    # Get the lowest test score.
    lowest = min(scores)

    # Subtract the lowest score from the total.
    total −= lowest

    # Calculate the average. Note that we divide
    # by 1 less than the number of scores because
    # the lowest score was dropped.
    average = total / (len(scores) − 1)

    # Display the average.
    print('The average, with the lowest score dropped',
    'is:', average)

# The get_scores function gets a series of test
# scores from the user and stores them in a list.
# A reference to the list is returned.
def get_scores():
    # Create an empty list.
    test_scores = []

    # Create a variable to control the loop.
    again = 'y'

    # Get the scores from the user and add them to
    # the list.
    while again == 'y':
        # Get a score and add it to the list.
        value = float(input('Enter a test score: '))
        test_scores.append(value)

        # Want to do this again?
        print('Do you want to add another score?')
        again = input('y = yes, anything else = no: ')
        print()

    # Return the list.
    return test_scores

# The get_total function accepts a list as an
# argument returns the total of the values in
# the list.
def get_total(value_list):
    # Create a variable to use as an accumulator.
    total = 0.0

    # Calculate the total of the list elements.
    for num in value_list:
        total += num

    # Return the total.
    return total

# Call the main function.
main()



# Working with liasts and files
# The writelines method - does not automatically write the '\n'

# writelines.py
# This program uses thewritelines method to save a list of strings to a file
def main():
    # Create a list of strings
    cities = ["New York", "Boston", "Atlanta", "Dalas"]
    
    # Open a flile for writing
    outfile = open("cities.txt", "w")
    
    # Write the list to the file
    outfile.writelines(cities)
    
    # Close the file
    outfile.close()

# Call the main function
main()

# After the program runs the citie.txt will containthe following line
New YorkBostonAtlantaDalas


# An alternative to the above program is to use a for loop and adding a new line character 

# This program saves a list to a file

def main():
    # Create a list of strings
    cities = ["New York", "Boston", "Atlanta", "Dalas"]

    # Open a flile for writing
    outfile = open("cities.txt", "w")
    
    # Write the list to the file
    for item in cities:
        outfile.write(item + "\n")
        
    # Close the file
    outfile.close()
    
# Call the main function
main()

# After the above program excecutes, thecities.txt file will contain the following lines

New York
Boston
Atlanta
Dalas

# Stripping the new line character
# This program reads a file's contents into a list

def main():
    # Open a file for reading
    infile = open("cities.txt", "r")
    
    # Read the contents of the file into a list
    cities = infile.readlines()
    
    # Close the file
    infile.close()
    
    # Strip the \n from each element
    index = 0
    while index < len(cities):
        cities[index] = cities[index].rstrip("\n")
        index += 1
    
    # Print the contents of the list
    print(cities)
    
# Call the main function
main()

# Program output
["New York", "Boston", "Atlanta", "Dalas"]



# Converting numbers into strings to write to file
# This program saves a list of numbers to a file.

def main():
    # Create a list of numbers.
    numbers = [1, 2, 3, 4, 5, 6, 7]

    # Open a file for writing.
    outfile = open('numberlist.txt', 'w')

    # Write the list to the file.
    for item in numbers:
        outfile.write(str(item) + '\n')

    # Close the file.
    outfile.close()

# Call the main function.
main()



# Reading a number list
# This program reads numbers from a file into a list.

def main():
    # Open a file for reading.
    infile = open('numberlist.txt', 'r')

    # Read the contents of the file into a list.
    numbers = infile.readlines()

    # Close the file.
    infile.close()

    # Convert each element to an int.
    index = 0
    while index < len(numbers):
        numbers[index] = int(numbers[index])
        index += 1

    # Print the contents of the list.
    print(numbers)

# Call the main function.
main()


# Two dimensional lists - Fill out later

repeats = 0
i = 1
while 


for variable in string:
    statement
    statement
    etc.



name = 'Juliet'
for ch in name:
    print(ch)



 1
# This program counts the number of times
 2
# the letter T (uppercase or lowercase)
 3
# appears in a string.
 4

 5
def main():
 6
# Create a variable to use to hold the count.
 7
# The variable must start with 0.
 8
count = 0
 9

10
# Get a string from the user.
11
my_string = input('Enter a sentence: ')
12

13
# Count the Ts.
14
for ch in my_string:
15
if ch == 'T' or ch == 't':
16
count += 1
17

18
# Print the result.
19
print('The letter T appears', count, 'times.')
20

21
# Call the main function.
22
main()



city = 'Boston'
index = 0
while index < len(city):
    print(city[index])
    index += 1




>>> message = 'Hello ' + 'world' [Enter]
>>> print(message) [Enter]
Hello world
>>>


# To get a slice of a string
string[start : end]




1
# The get_login_name function accepts a first name,
 2
# last name, and ID number as arguments. It returns
 3
# a system login name.
 4

 5
def get_login_name(first, last, idnumber):
 6
# Get the first three letters of the first name.
 7
# If the name is less than 3 characters, the
 8
# slice will return the entire first name.
 9
set1 = first[0 : 3]
10

11
# Get the first three letters of the last name.
12
# If the name is less than 3 characters, the
13
# slice will return the entire last name.
14
set2 = last[0 : 3]
15

16
# Get the last three characters of the student ID.
17
# If the ID number is less than 3 characters, the
18
# slice will return the entire ID number.
19
set3 = idnumber[-3 :]
20

21
# Put the sets of characters together.
22
login_name = set1 + set2 + set3
23

24
# Return the login name.
25
return login_name



# Is string 1 in string 2?
string1 in string2

text = 'Four score and seven years ago'
if 'seven' in text:
    print('The string "seven" was found.') 
else:
    print('The string "seven" was not found.')



names = 'Bill Joanne Susan Chris Juan Katie'
 if 'Pierre' not in names:
     print('Pierre was not found.')
 else:
     print('Pierre was found.')


string1 = '1200'
if string1.isdigit():
    print(string1, 'contains only digits.')
else:
    print(string1, 'contains characters other than digits.')



Method	Description
isalnum()	Returns true if the string contains only alphabetic letters or digits and is at least one character in length. Returns false otherwise.
isalpha()	Returns true if the string contains only alphabetic letters and is at least one character in length. Returns false otherwise.
isdigit()	Returns true if the string contains only numeric digits and is at least one character in length. Returns false otherwise.
islower()	Returns true if all of the alphabetic letters in the string are lowercase, and the string contains at least one alphabetic letter. Returns false otherwise.
isspace()	Returns true if the string contains only whitespace characters and is at least one character in length. Returns false otherwise. (Whitespace characters are spaces, newlines (\n), and tabs (\t).
isupper()	Returns true if all of the alphabetic letters in the string are uppercase, and the string contains at least one alphabetic letter. Returns false otherwise.


 1
# This program demonstrates several string testing methods.
 2

 3
def main():
 4
# Get a string from the user.
 5
user_string = input('Enter a string: ')
 6

 7
print('This is what I found about that string:')
 8

 9
# Test the string.
10
if user_string.isalnum():
11
print('The string is alphanumeric.')
12
if user_string.isdigit():
13
print('The string contains only digits.')
14
if user_string.isalpha():
15
print('The string contains only alphabetic characters.')
16
if user_string.isspace():
17
print('The string contains only whitespace characters.')
18
if user_string.islower():
19
print('The letters in the string are all lowercase.')
20
if user_string.isupper():
21
print('The letters in the string are all uppercase.')
22

23
# Call the main function.
24
main()


Method	Description
lower()	Returns a copy of the string with all alphabetic letters converted to lowercase. Any character that is already lowercase, or is not an alphabetic letter, is unchanged.
lstrip()	Returns a copy of the string with all leading whitespace characters removed. Leading whitespace characters are spaces, newlines (\n), and tabs (\t) that appear at the beginning of the string.
lstrip(char)	The char argument is a string containing a character. Returns a copy of the string with all instances of char that appear at the beginning of the string removed.
rstrip()	Returns a copy of the string with all trailing whitespace characters removed. Trailing whitespace characters are spaces, newlines (\n), and tabs (\t) that appear at the end of the string.
rstrip(char)	The char argument is a string containing a character. The method returns a copy of the string with all instances of char that appear at the end of the string removed.
strip()	Returns a copy of the string with all leading and trailing whitespace characters removed.
strip(char)	Returns a copy of the string with all instances of char that appear at the beginning and the end of the string removed.
upper()	Returns a copy of the string with all alphabetic letters converted to uppercase. Any character that is already uppercase, or is not an alphabetic letter, is unchanged.


letters = 'WXYZ'
print(letters, letters.lower())



again = 'y'
while again.lower() == 'y':
    print('Hello')
    print('Do you want to see that again?')
    again = input('y = yes, anything else = no: ')



Method	Description
endswith(substring)	The substring argument is a string. The method returns true if the string ends with substring.
find(substring)	The substring argument is a string. The method returns the lowest index in the string where substring is found. If substring is not found, the method returns −1.
replace(old, new)	The old and new arguments are both strings. The method returns a copy of the string with all instances of old replaced by new.
startswith(substring)	The substring argument is a string. The method returns true if the string starts with substring.

filename = input('Enter the filename: ')
if filename.endswith('.txt'):
    print('That is the name of a text file.')
elif filename.endswith('.py'):
    print('That is the name of a Python source file.')
elif filename.endswith('.doc'):
    print('That is the name of a word processing document.')
else:
    print('Unknown file type.')




string = 'Four score and seven years ago'
position = string.find('seven')
if position != −1:
    print('The word "seven" was found at index', position)
else:
    print('The word "seven" was not found.')

The word "seven" was found at index 15


string = 'Four score and seven years ago'
new_string = string.replace('years', 'days')
print(new_string)

















# Dictionaries

# Create or Update single line for loop

counts = dict()
names = ['scev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    counts[name] = counts.get(name.get(name, 0) + 1
print(counts)






# Definite loops and dictionaries

counts = { 'chuck' : 1 , 'fred' : 42, 'jan' : 100}
for key in counts:
    print(key, counts[key])
    
    
jan 100
chuck 1
fred 42



# Retrieving lists of keys and values

jjj = { 'chuck' : 1 , 'fred' : 42, 'jan' : 100}
print(list(jjj))
['jan', 'chuck', 'fred']
print(jjj.keys())
['jan', 'chuck', 'fred']
print(jjj.values())
[100, 1, 42]
print(jjj.items())
[('jan', 100), ('chuck', 1), ('fred', 42)]



# Bonus: Two iteration Variables
# We loop through the key-value pairs in a dictionary using *two* iteration variables

jjj = { 'chuck' : 1 , 'fred' : 42, 'jan' : 100}
for aaa,bbb in jjj.items() :
    print(aaa, bbb)
    
# Each iteration, the first variable is the key and the second variable is the corresponding value for the key

jan 100
chuck 1
fred 42


name = input('Enter file:')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word inwords:
        counts[word] = counts.get(word,0) + 1


# Finding the largest pairs in the key value dictionary
bigcount = None
bigword = None
for word,count in counts.items():
    # Max loop
    if bigcount is None or count > bigcoun:
        bigword = word
        bigcount = count
        
print(bigword, bigcount)



# Dictionary creation
phonebook = {'Chris':'555−1111', 'Katie':'555−2222', 'Joanne':'555−3333'}

phonebook [Enter]
{'Chris': '555−1111', 'Joanne': '555−3333', 'Katie': '555−2222'}

# You cannot use a numeric index to retrieve a value by its position from a dictionary. Instead, you use a key to retrieve a value.

# To retrieve a value from a dictionary, you simply write an expression in the following general format:

dictionary_name[key]

#If the key does not exist, a KeyError exception is raised

# Using 'in' and 'not in' in order to prevent exception
phonebook = {'Chris':'555−1111', 'Katie':'555−2222','Joanne':'555−3333'} [Enter]
    if 'Chris' in phonebook:
      print(phonebook['Chris'])
555−1111

if 'Joanne' not in phonebook:
        print('Joanne is not found.')
        
Joanne is not found.

# Adding elements to an existing Dictionary
dictionary_name[key] = value


# If key already exists in the dictionary, its associated value will be changed to value. If the key does not exist, it will be added to the dictionary, along with value as its associated value.

>>> phonebook = {'Chris':'555−1111', 'Katie':'555−2222', 'Joanne':'555−3333'} [Enter]
>>> phonebook['Joe'] = '555−0123' [Enter]
>>> phonebook['Chris'] = '555−4444' [Enter]
>>> phonebook [Enter]
{'Chris': '555−4444', 'Joanne': '555−3333', 'Joe': '555−0123', 'Katie': '555−2222'}
>>>

# Deleting element or key-value pairs
del dictionary_name[key]

del phonebook['Chris'] [Enter]
 >>> phonebook [Enter]
 {'Joanne': '555−3333', 'Katie': '555−2222'}

>>> phonebook = {'Chris':'555−1111', 'Katie':'555−2222', 'Joanne':'555−3333'} [Enter]
>>> if 'Chris' in phonebook: [Enter]
      del phonebook['Chris'] [Enter] [Enter]
>>> phonebook [Enter]
{'Joanne': '555−3333', 'Katie': '555−2222'}
>>> 

# Getting the number of elements in a dictionary or its lenght
>>> phonebook = {'Chris':'555−1111', 'Katie':'555−2222'} [Enter]
>>> num_items = len(phonebook) [Enter]
>>> print(num_items) [Enter]


# In this session, we create a dictionary in which the keys are student names, and the values are lists of test scores.
>>> test_scores = { 'Kayla' : [88, 92, 100], [Enter]
                'Luis' : [95, 74, 81], [Enter]
                'Sophie' : [72, 88, 91], [Enter]
                'Ethan' : [70, 75, 78] } [Enter]
>>> test_scores [Enter]
{'Kayla': [88, 92, 100], 'Sophie': [72, 88, 91], 'Ethan': [70, 75, 78],
'Luis': [95, 74, 81]}
>>> test_scores['Sophie'] [Enter]
[72, 88, 91]
>>> kayla_scores = test_scores['Kayla'] [Enter]
>>> print(kayla_scores) [Enter]
[88, 92, 100]

# Creating an empty dictionary
phonebook = dict()

# Iterating over a dictionary
for var in dictionary:
          statement
          statement 
          etc.

# Different types mixed in a dictionary
>>> mixed_up = {'abc':1, 999:'yada yada', (3, 6, 9):[3, 6, 9]} [Enter]
>>> mixed_up [Enter]
{(3, 6, 9): [3, 6, 9], 'abc': 1, 999: 'yada yada'}

employee = {'name' : 'Kevin Smith', 'id' : 12345, 'payrate' : 25.75 } [Enter]
>>> employee [Enter]
{'payrate': 25.75, 'name': 'Kevin Smith', 'id': 12345}
>>>


# Some dictionary methods
clear	Clears the contents of a dictionary.
get	Gets the value associated with a specified key. If the key is not found, the method does not raise an exception. Instead, it returns a default value.
items	Returns all the keys in a dictionary and their associated values as a sequence of tuples.
keys	Returns all the keys in a dictionary as a sequence of tuples.
pop	Returns the value associated with a specified key and removes that key-value pair from the dictionary. If the key is not found, the method returns a default value.
﻿popitem	Returns a randomly selected key-value pair as a tuple from the dictionary and removes that key-value pair from the dictionary.
values	Returns all the values in the dictionary as a sequence of tuples.





# The clearMethod
dictionary.clear()


# The get Method - The get method does not raise an exception if the specified key is not found. Here is the method’s general format:
dictionary.get(key, default)

# The items Method - If we call the phonebook.items() method, it returns the following sequence:

[('Chris', '555−1111'), ('Joanne', '555−3333'), ('Katie', '555−2222')]


# Using a for loop to print all item sets in dictionary
for key, value in phonebook.items(): [Enter]
         print(key, value) [Enter] [Enter]
Chris 555−1111
Joanne 555−3333
Katie 555−2222

# The keys Method - If we call the  method, it will return the following sequence:

phonebook.keys()
['Chris', 'Joanne', 'Katie']

The following interactive session shows how you can use a for loop to iterate over the sequence that is returned from the keys method:

>>> phonebook = {'Chris':'555−1111', [Enter]
                 'Katie':'555−2222', [Enter]
                 'Joanne':'555−3333'} [Enter]
>>> for key in phonebook.keys(): [Enter]
        print(key) [Enter] [Enter]
Chris
Joanne
Katie

# The pop Method

dictionary.pop(key, default)

# When the method is called, it returns the value that is associated with the specified key, and it removes that key-value pair from the dictionary. If the specified key is not found in the dictionary, the method returns default. The following interactive session demonstrates:

phonebook = {'Chris':'555−1111', [Enter]
                  'Katie':'555−2222', [Enter]
                  'Joanne':'555−3333'} [Enter]
>>> phone_num = phonebook.pop('Chris', 'Entry not found') [Enter]
>>> phone_num [Enter]
'555−1111'
>>> phonebook [Enter]
{'Joanne': '555−3333', 'Katie': '555−2222'}
>>> phone_num = phonebook.pop('Andy', 'Element not found') [Enter]
>>> phone_num [Enter]
'Element not found'
>>> phonebook [Enter]
{'Joanne': '555−3333', 'Katie': '555−2222'}

# The popitem Method - The popitem method returns a randomly selected key-value pair, and it removes that key-value pair from the dictionary. The key-value pair is returned as a tuple.

dictionary.popitem()

# You can use an assignment statement in the following general format to assign the returned key and value to individual variables:

k, v = dictionary.popitem()

# The values Method - The values method returns all a dictionary’s values
phonebook.values()
['555−1111', '555−2222', '555−3333']
for val in phonebook.values(): [Enter]
       print(val) [Enter] [Enter]










# Card dealer program
# This program uses a dictionary as a deck of cards.

def main():
    # Create a deck of cards.
    deck = create_deck()

    # Get the number of cards to deal.
    num_cards = int(input('How many cards should I deal? '))

    # Deal the cards.
    deal_cards(deck, num_cards)

    # The create_deck function returns a dictionary
    # representing a deck of cards.
    def create_deck():
    # Create a dictionary with each card and its value
    # stored as key-value pairs.
    deck = {'Ace of Spades':1, '2 of Spades':2, '3 of Spades':3,
    '4 of Spades':4, '5 of Spades':5, '6 of Spades':6,
    '7 of Spades':7, '8 of Spades':8, '9 of Spades':9,
    '10 of Spades':10, 'Jack of Spades':10,
    'Queen of Spades':10, 'King of Spades': 10,

    'Ace of Hearts':1, '2 of Hearts':2, '3 of Hearts':3,
    '4 of Hearts':4, '5 of Hearts':5, '6 of Hearts':6,
    '7 of Hearts':7, '8 of Hearts':8, '9 of Hearts':9,
    '10 of Hearts':10, 'Jack of Hearts':10,
    'Queen of Hearts':10, 'King of Hearts': 10,

    'Ace of Clubs':1, '2 of Clubs':2, '3 of Clubs':3,
    '4 of Clubs':4, '5 of Clubs':5, '6 of Clubs':6,
    '7 of Clubs':7, '8 of Clubs':8, '9 of Clubs':9,
    '10 of Clubs':10, 'Jack of Clubs':10,
    'Queen of Clubs':10, 'King of Clubs': 10,

    'Ace of Diamonds':1, '2 of Diamonds':2, '3 of Diamonds':3,
    '4 of Diamonds':4, '5 of Diamonds':5, '6 of Diamonds':6,
    '7 of Diamonds':7, '8 of Diamonds':8, '9 of Diamonds':9,
    '10 of Diamonds':10, 'Jack of Diamonds':10,
    'Queen of Diamonds':10, 'King of Diamonds': 10}

    # Return the deck.

    return deck

# The deal_cards function deals a specified number of cards
# from the deck.
def deal_cards(deck, number):

    # Initialize an accumulator for the hand value.
    hand_value = 0

    # Make sure the number of cards to deal is not
    # greater than the number of cards in the deck.
    if number > len(deck):
    number = len(deck)

    # Deal the cards and accumulate their values.
    for count in range(number):
    card, value = deck.popitem()
    print(card)
    hand_value += value

# Display the value of the hand.
print('Value of this hand:', hand_value)

# Call the main function.
main()




# Birthday Menu Options and Functions

# This program uses a dictionary to keep friends'
# names and birthdays.

# Global constants for menu choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
 QUIT = 5

# main function
def main():
# Create an empty dictionary.
birthdays = {}

# Initialize a variable for the user's choice.
choice = 0

while choice != QUIT:
# Get the user's menu choice.
choice = get_menu_choice()

# Process the choice.
if choice == LOOK_UP:
look_up(birthdays)
elif choice == ADD:
add(birthdays)
elif choice == CHANGE:
change(birthdays)
elif choice == DELETE:
delete(birthdays)

# The get_menu_choice function displays the menu
# and gets a validated choice from the user.
def get_menu_choice():
print()
print('Friends and Their Birthdays')
print('---------------------------')
print('1. Look up a birthday')
print('2. Add a new birthday')
print('3. Change a birthday')
print('4. Delete a birthday')
print('5. Quit the program')
print()

# Get the user's choice.
choice = int(input('Enter your choice: '))

# Validate the choice.
while choice < LOOK_UP or choice > QUIT:
choice = int(input('Enter a valid choice: '))

# return the user's choice.
return choice

# The look_up function looks up a name in the
# birthdays dictionary.
def look_up(birthdays):
# Get a name to look up.
name = input('Enter a name: ')

# Look it up in the dictionary.
print(birthdays.get(name, 'Not found.'))

# The add function adds a new entry into the
# birthdays dictionary.
def add(birthdays):
# Get a name and birthday.
name = input('Enter a name: ')
bday = input('Enter a birthday: ')

# If the name does not exist, add it.
if name not in birthdays:
birthdays[name] = bday
else:
print('That entry already exists.')

# The change function changes an existing
# entry in the birthdays dictionary.
def change(birthdays):
# Get a name to look up.
name = input('Enter a name: ')

if name in birthdays:
# Get a new birthday.
bday = input('Enter the new birthday: ')

# Update the entry.
birthdays[name] = bday
else:
print('That name is not found.’)

# The delete function deletes an entry from the
# birthdays dictionary.
def delete(birthdays):
# Get a name to look up.
name = input('Enter a name: ')

# If the name is found, delete the entry.
if name in birthdays:
del birthdays[name]
else:
print('That name is not found.')

# Call the main function.
main()



# retrieves from the dictionary the value that is associated with the key 'answer'.
d.get('answer')

# Write a statement that assigns the value 'Python' to the key 'Monty'.
d['Monty'] = 'Python'

# Assume there is a variable, album_artists, that refers to a dictionary that maps albums to performing artists. Write a statement that inserts the key/value pair: 'Live It Out' / 'Metric'.
album_artists['Live It Out'] = 'Metric'

# Assume the variable us_cabinet refers to a dictionary that maps department names to department heads. Write a statement that assigns the value 'Mukasey' to the key 'Justice Department'.
us_cabinet['Justice Department'] = 'Mukasey'

# Assume the variable planet_distances refers to a dictionary that maps planet names to planetary distances from the sun. Write a statement that deletes the element with the key 'Pluto'.
del(planet_distances['Pluto'])



#Assume three dictionaries are assigned to the variables, canadian_capitals, mexican_capitals, and us_capitals. These dictionaries map provinces or states to their respective capitals. Write code that creates a new dictionary that combines these three dictionaries, and associate it with a variable named nafta_capitals.
nafta_capitals = {**canadian_capitals, **mexican_capitals, **us_capitals}

# Given a dictionary d, create a new dictionary that reverses the keys and values of d. Thus, the keys of d become the values of the new dictionary and the values of d become the keys of the new dictionary. You may assume d contains no duplicate values (that is, no two keys map to the same values.) Associate the new dictionary with the variable inverse.
inverse = {v: k for k, v in d.items()}

# Given the dictionary, d, find the largest key in the dictionary and assign its value to the variable val_of_max. For example, given the dictionary {5:3, 4:1, 12:2}, the value 2 would be assigned to val_of_max. Assume d is not empty.
val_of_max = d[max(d)]

# Create a dictionary that maps the first n counting numbers to their squares. Assign the dictionary to the variable squares.
squares = {}
for x in range(1, n + 1):
    squares[x] = x * x
    
# Assume you have two lists named list1 and list2 that are of the same length. Create a dictionary in which the elements of list1 are the keys and the elements of list2 are the values. For example, the dictionary will have:

# an element in which list1[0] is the key and list2[0] is the value,
# an element in which list1[1] is the key and list2[1] is the value,
# and so on.
dict1 = dict([(list1[i], list2[i]) for i in range(len(list1))])


# Sets

# Creating an empty set
myset = set()

# Passing arguments into set
myset = set(['a', 'b', 'c'])

# Adding elements with myset.add()
myset.add(1)

# the myset variable will reference a set containing the elements 'a', 'b', and 'c'
myset = set('abc')

# No duplicate elements in sets
myset = set('aaabc')
# 'a', 'b', and 'c'

# This is an ERROR! - only one argument allowed
myset = set('one', 'two', 'three')

# This does not do what we intend.
myset = set('one two three')
# 'o', 'n', 'e', '', 't', 'w', 'h', and 'r'

# OK, this works.
myset = set(['one', 'two', 'three'])



# Getting the Number of Elements in a Set
>>> myset = set([1, 2, 3, 4, 5]) [Enter]
>>> len(myset) [Enter]
5

# Adding and Removing Elements
myset.add(1)
myset.remove(1) - # May cause exception if element is non existent
myset.discard(1) - # Does not throw an exception if element is not found

myset.clear() - # Clears all elements in the set

# add a group of elements to a set all at one time
>>> myset = set([1, 2, 3]) [Enter]
>>> myset.update([4, 5, 6]) [Enter]
>>> myset [Enter]
{1, 2, 3, 4, 5, 6}
>>>


# Using the for Loop to Iterate over a Set
for var in set:
     statement
     statement
     etc.

>>> myset = set(['a', 'b', 'c']) [Enter]
>>> for val in myset: [Enter]
        print(val) [Enter] [Enter]
a
c
b

# Using the in and not in Operators to Test for a Value in a Set
>>> myset = set([1, 2, 3]) [Enter]
>>> if 1 in myset: [Enter]
         print('The value 1 is in the set.') [Enter] [Enter]
The value 1 is in the set.

>>> myset = set([1, 2, 3]) [Enter]
>>> if 99 not in myset: [Enter]
       print('The value 99 is not in the set.') [Enter] [Enter]
The value 99 is not in the set.

# Finding the Union of Sets
# The union of two sets is a set that contains all the elements of both sets. In Python, you can call the union method to get the union of two sets. Here is the general format:

set1.union(set2)

>>> set1 = set([1, 2, 3, 4]) [Enter]
>>> set2 = set([3, 4, 5, 6]) [Enter]
>>> set3 = set1.intersection(set2) [Enter]
>>> set3 [Enter]
{3, 4}

# You can also use the & operator to find the intersection of two sets. Here is the general format of an expression using the & operator with two sets:

set1 & set2

>>> set1 = set([1, 2, 3, 4]) [Enter]
>>> set2 = set([3, 4, 5, 6]) [Enter]
>>> set3 = set1 & set2 [Enter]
>>> set3 [Enter]
{3, 4}

# Finding the Difference of Sets
# The difference of set1 and set2 is the elements that appear in set1 but do not appear in set2. In Python, you can call the difference method to get the difference of two sets. Here is the general format:

set1.difference(set2)

>>> set1 = set([1, 2, 3, 4]) [Enter]
>>> set2 = set([3, 4, 5, 6]) [Enter]
>>> set3 = set1.difference(set2) [Enter]
>>> set3 [Enter]
{1, 2}

# You can also use the − operator to find the difference of two sets. Here is the general format of an expression using the − operator with two sets:

set1 − set2

>>> set1 = set([1, 2, 3, 4]) [Enter]
>>> set2 = set([3, 4, 5, 6]) [Enter]
>>> set3 = set1 − set2 [Enter]
>>> set3 [Enter]
{1, 2}

# Finding the Symmetric Difference of Sets
# The symmetric difference of two sets is a set that contains the elements that are not shared by the sets. In other words, it is the elements that are in one set but not in both. In Python, you can call the symmetric_difference method to get the symmetric difference of two sets. Here is the general format:

set1.symmetric_difference(set2)
set1 ˆ set2 - # Same thing

# The method returns a set that contains the elements that are found in either set1 or set2 but not both sets. The following interactive session demonstrates:

>>> set1 = set([1, 2, 3, 4]) [Enter]
>>> set2 = set([3, 4, 5, 6]) [Enter]
>>> set3 = set1.symmetric_difference(set2) [Enter]
>>> set3 [Enter]
{1, 2, 5, 6}

# Finding Subsets and Supersets
# Suppose you have two sets, and one of those sets contains all of the elements of the other set. Here is an example:

set1 = set([1, 2, 3, 4])
set2 = set([2, 3])

# In this example, set1 contains all the elements of set2, which means that set2 is a subset of set1. It also means that set1 is a superset of set2. In Python, you can call the issubset method to determine whether one set is a subset of another. Here is the general format:

set2.issubset(set1)

# In the general format, set1 and set2 are sets. The method returns True if set2 is a subset of set1. Otherwise, it returns False. You can call the issuperset method to determine whether one set is a superset of another. Here is the general format:

set1.issuperset(set2)

# In the general format, set1 and set2 are sets. The method returns True if set1 is a superset of set2. Otherwise, it returns False. The following interactive session demonstrates:

>>> set1 = set([1, 2, 3, 4]) [Enter]
>>> set2 = set([2, 3]) [Enter]
>>> set2.issubset(set1) [Enter]
True
>>> set1.issuperset(set2) [Enter]
True
>>> 

# You can also use the <= operator to determine whether one set is a subset of another and the >= operator to determine whether one set is a superset of another. Here is the general format of an expression using the <= operator with two sets:

set2 <= set1

# In the general format, set1 and set2 are sets. The expression returns True if set2 is a subset of set1. Otherwise, it returns False. Here is the general format of an expression using the >= operator with two sets:

set1 >= set2

# In the general format, set1 and set2 are sets. The expression returns True if set1 is a subset of set2. Otherwise, it returns False. The following interactive session demonstrates:

>>> set1 = set([1, 2, 3, 4]) [Enter]
>>> set2 = set([2, 3]) [Enter]
>>> set2 <= set1 [Enter]
True
>>> set1 >= set2 [Enter]
True
>>> set1 <= set2 [Enter]
False 

# In the Spotlight: Set Operations
# In this section, you will look at Program 9-3, which demonstrates various set operations. The program creates two sets: one that holds the names of students on the baseball team, and another that holds the names of students on the basketball team. The program then performs the following operations:

# It finds the intersection of the sets to display the names of students who play both sports.

# It finds the union of the sets to display the names of students who play either sport.

# It finds the difference of the baseball and basketball sets to display the names of students who play baseball but not basketball.

# It finds the difference of the basketball and baseball (basketball – baseball) sets to display the names of students who play basketball but not baseball. It also finds the difference of the baseball and basketball (baseball – basketball) sets to display the names of students who play baseball but not basketball.

# It finds the symmetric difference of the basketball and baseball sets to display the names of students who play one sport but not both.

# In the animation below, press the “Previous” or “Next” button to step through the code and see explanations throughout.

Program 9-3
(sets.py)

# This program demonstrates various set operations.
baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])

# Display members of the baseball set.
print('The following students are on the baseball team:')
    for name in baseball:
        print(name)

# Display members of the basketball set.
print()
print('The following students are on the basketball team:')
for name in basketball:
    print(name)
        
# Demonstrate intersection
print()
print('The following students play both baseball and basketball:')
for name in baseball.intersection(basketball):
    print(name)

# Demonstrate union
print()
print('The following students play either baseball or basketball:')
for name in baseball.union(basketball):
    print(name)

# Demonstrate difference of baseball and basketball
print()
print('The following students play baseball, but not basketball:')
for name in baseball.difference(basketball):
    print(name)

# Demonstrate difference of basketball and baseball
print()
print('The following students play basketball, but not baseball:')
for name in basketball.difference(baseball):
    print(name)

# Demonstrate symmetric difference
print()
print('The following students play one sport, but not both:')
for name in baseball.symmetric_difference(basketball):
    print(name)


# Making and printing key values from dictionaries
CL_ROOM_NUMBERS = { 'CS101' : 3004, 'CS102' : 4501, 'CS103' : 6755, 'NT110' : 1244, 'CM241' : 1411 }
CL_INSTRUCTORS = { 'CS101' : 'Haynes', 'CS102' : 'Alvarado', 'CS103' : 'Rich', 'NT110' : 'Burke', 'CM241' : 'Lee' }
CL_MEETING_TIMES = { 'CS101' : '8:00am', 'CS102' : '9:00am', 'CS103' : '10:00am', 'NT110' : '11:00am', 'CM241' : '1:00pm' }
class_name = input('Enter a class name:')
print('Class:', class_name)
print('Room:', CL_ROOM_NUMBERS[class_name])
print('Instructor:', CL_INSTRUCTORS[class_name])
print('Time:', CL_MEETING_TIMES[class_name])






# Classes

 import random
 # The Coin class simulates a coin that can
 # be flipped.
 class Coin:
     # The _ _init_ _ method initializes the
     # sideup data attribute with 'Heads'.
     def _ _init_ _(self):
         self.sideup = 'Heads'
     # The toss method generates a random number
     # in the range of 0 through 1. If the number
     # is 0, then sideup is set to 'Heads'.
     # Otherwise, sideup is set to 'Tails'.
     def toss(self):
         if random.randint(0, 1) == 0:
             self.sideup = 'Heads'
         else:
             self.sideup = 'Tails'
     # The get_sideup method returns the value
     # referenced by sideup.
     def get_sideup(self):
         return self.sideup 



import random
 # The Coin class simulates a coin that can
 # be flipped.
 class Coin:
     # The _ _init_ _ method initializes the
     # sideup data attribute with 'Heads'.
     def _ _init_ _(self):
         self.sideup = 'Heads'
     # The toss method generates a random number
     # in the range of 0 through 1. If the number
     # is 0, then sideup is set to 'Heads'.
     # Otherwise, sideup is set to 'Tails'.
     def toss(self):
         if random.randint(0, 1) == 0:
             self.sideup = 'Heads'
         else:
             self.sideup = 'Tails'
     # The get_sideup method returns the value
     # referenced by sideup.
     def get_sideup(self):
         return self.sideup
 # The main function.
 def main():
     # Create an object from the Coin class.
     my_coin = Coin()
     # Display the side of the coin that is facing up.
     print('This side is up:', my_coin.get_sideup())
     # Toss the coin.
     print('I am tossing the coin ...')
     my_coin.toss()
     # Display the side of the coin that is facing up.
     print('This side is up:', my_coin.get_sideup())
 # Call the main function.
 main() 


import random
 # The Coin class simulates a coin that can
 # be flipped.
 class Coin:
     # The _ _init_ _ method initializes the
     # _ _sideup data attribute with ‘Heads’.
     def _ _init_ _(self):
     self._ _sideup = 'Heads'
     # The toss method generates a random number
     # in the range of 0 through 1. If the number
     # is 0, then sideup is set to 'Heads'.
     # Otherwise, sideup is set to 'Tails'.
     def toss(self):
         if random.randint(0, 1) == 0:
             self._ _sideup = 'Heads'
         else:
             self._ _sideup = 'Tails'
     # The get_sideup method returns the value
     # referenced by sideup.
     def get_sideup(self):
         return self._ _sideup  # Private attribute
 # The main function.
 def main():
     # Create an object from the Coin class.
     my_coin = Coin()
     # Display the side of the coin that is facing up.
     print('This side is up:', my_coin.get_sideup())
     # Toss the coin.
     print('I am going to toss the coin ten times:')
     for count in range(10):
         my_coin.toss()
         print(my_coin.get_sideup())
  # Call the main function.
  main() 




# Coin module
import random
 2

 3
# The Coin class simulates a coin that can
 4
# be flipped.
 5

 6
class Coin:
 7

 8
# The __init__ method initializes the
 9
# __sideup data attribute with 'Heads'.
10

11
def __init__(self):
12
self.__sideup = 'Heads'
13

14
# The toss method generates a random number
15
# in the range of 0 through 1. If the number
16
# is 0, then sideup is set to 'Heads'.
17
# Otherwise, sideup is set to 'Tails'.
18

19
def toss(self):
20
if random.randint(0, 1) == 0:
21
self.__sideup = 'Heads'
22
else:
23
self.__sideup = 'Tails'
24

25
# The get_sideup method returns the value
26
# referenced by sideup.
27

28
def get_sideup(self):
29
return self.__sideup




# Coin demo
 1
# This program imports the coin module and
 2
# creates an instance of the Coin class.
 3

 4
import coin
 5

 6
def main():
 7
# Create an object from the Coin class.
 8
my_coin = coin.Coin()                                       # Using Coin class from coin Module
 9

10
# Display the side of the coin that is facing up.
11
print('This side is up:', my_coin.get_sideup())
12

13
# Toss the coin.
14
print('I am going to toss the coin ten times:')
15
for count in range(10):
16
my_coin.toss()
17
print(my_coin.get_sideup())
18

19
# Call the main function.
20
main()



# BankAccount Class with two parameters

  # The BankAccount class simulates a bank account.
  class BankAccount:
      # The _ _init_ _ method accepts an argument for
      # the account's balance. It is assigned to
      # the _ _balance attribute.
      def _ _init_ _(self, bal):
          self._ _balance = bal
      # The deposit method makes a deposit into the
      # account.
      def deposit(self, amount):
          self._ _balance += amount
      # The withdraw method withdraws an amount
      # from the account.
      def withdraw(self, amount):
          if self._ _balance >= amount:
              self._ _balance −= amount
          else:
              print('Error: Insufficient funds')
      # The get_balance method returns the
      # account balance.
  def get_balance(self):
      return self._ _balance 

# Using the Class
  # This program demonstrates the BankAccount class.  
  import bankaccount
  def main():
      # Get the starting balance.
      start_bal = float(input('Enter your starting balance: ')) 
      # Create a BankAccount object.
      savings = bankaccount.BankAccount(start_bal)
      # Deposit the user's paycheck.
      pay = float(input('How much were you paid this week? '))
      print('I will deposit that into your account.')
      savings.deposit(pay)
      # Display the balance.
      print('Your account balance is $',
            format(savings.get_balance(), ',.2f'),
            sep='')
      # Get the amount to withdraw.
      cash = float(input('How much would you like to withdraw? '))
      print('I will withdraw that from your account.')
      savings.withdraw(cash)
      # Display the balance.
      print('Your account balance is $', 
            format(savings.get_balance(), ',.2f'),
            sep='')
  # Call the main function.
  
  
  
  # Displaying an object’s state is a common task. It is so common that many programmers equip their classes with a method that returns a string containing the object’s state. In Python, you give this method the special name _ _str_ _.
  
  1
# The BankAccount class simulates a bank account.
 2

 3
class BankAccount:
 4

 5
# The __init__ method accepts an argument for
 6
# the account's balance. It is assigned to
 7
# the __balance attribute.
 8

 9
def __init__(self, bal):
10
self.__balance = bal
11

12
# The deposit method makes a deposit into the
13
# account.
14

15
def deposit(self, amount):
16
self.__balance += amount
17

18
# The withdraw method withdraws an amount
19
# from the account.
20

21
def withdraw(self, amount):
22
if self.__balance >= amount:
23
self.__balance -= amount
24
else:
25
print('Error: Insufficient funds')
26

27
# The get_balance method returns the
28
# account balance.
29

30
def get_balance(self):
31
return self.__balance
32

33
# The __str__ method returns a string
34
# indicating the object's state.
35

36
def __str__(self):
37
return 'The balance is $' + format(self.__balance, ',.2f')


# Cellphone Class
 1
# The CellPhone class holds data about a cell phone.
 2

 3
class CellPhone:
 4

 5
# The __init__ method initializes the attributes.
 6

 7
def __init__(self, manufact, model, price):
 8
self.__manufact = manufact
 9
self.__model = model
10
self.__retail_price = price
11

12
# The set_manufact method accepts an argument for
13
# the phone's manufacturer.
14

15
def set_manufact(self, manufact):
16
self.__manufact = manufact
17

18
# The set_model method accepts an argument for
19
# the phone's model number.
20

21
def set_model(self, model):
22
self.__model = model
23

24
# The set_retail_price method accepts an argument
25
# for the phone's retail price.
26

27
def set_retail_price(self, price):
28
self.__retail_price = price
29

30
# The get_manufact method returns the
31
# phone's manufacturer.
32

33
def get_manufact(self):
34
return self.__manufact
35

36
# The get_model method returns the
37
# phone's model number.
38

39
def get_model(self):
40
return self.__model
41

42
# The get_retail_price method returns the
43
# phone's retail price.
44

45
def get_retail_price(self):
46
return self.__retail_pricev







 1
# This program tests the CellPhone class.
 2

 3
import cellphone
 4

 5
def main():
 6
# Get the phone data.
 7
man = input('Enter the manufacturer: ')
 8
mod = input('Enter the model number: ')
 9
retail = float(input('Enter the retail price: '))
10

11
# Create an instance of the CellPhone class.
12
phone = cellphone.CellPhone(man, mod, retail)
13

14
# Display the data that was entered.
15
print('Here is the data that you entered:')
16
print('Manufacturer:', phone.get_manufact())
17
print('Model Number:', phone.get_model())
18
print('Retail Price: $', format(phone.get_retail_price(), ',.2f'), sep='')
19

20
# Call the main function.
21
main()

...

cellphone.py

...

3
class CellPhone:
4

5
# The __init__ method initializes the attributes.
6

7
def __init__(self, manufact, model, price):
8
self.__manufact = manufact
9
self.__model = model
10
self.__retail_price = price
11

12
# The set_manufact method accepts an argument for
13
# the phone's manufacturer.
14

15
def set_manufact(self, manufact):
16
self.__manufact = manufact
17

18
# The set_model method accepts an argument for
19
# the phone's model number.
20

21
def set_model(self, model):
22
self.__model = model
23

24
# The set_retail_price method accepts an argument
25
# for the phone's retail price.
26

27
def set_retail_price(self, price):
28
self.__retail_price = price
29

30
# The get_manufact method returns the
31
# phone's manufacturer.
32

33
def get_manufact(self):
34
return self.__manufact
35

36
# The get_model method returns the
37
# phone's model number.
38

39
def get_model(self):
40
return self.__model
41

42
# The get_retail_price method returns the
43
# phone's retail price.
44

45
def get_retail_price(self):
46
return self.__retail_price





# Storing Objects in a List
 1
# This program creates five CellPhone objects and
 2
# stores them in a list.
 3

 4
import cellphone
 5

 6
def main():
 7
# Get a list of CellPhone objects.
 8
phones = make_list()
 9

10
# Display the data in the list.
11
print('Here is the data you entered:')
12
display_list(phones)
13

14
# The make_list function gets data from the user
15
# for five phones. The function returns a list
16
# of CellPhone objects containing the data.
17

18
def make_list():
19
# Create an empty list.
20
phone_list = []
21

22
# Add five CellPhone objects to the list.
23
print('Enter data for five phones.')
24
for count in range(1, 6):
25
# Get the phone data.
26
print('Phone number ' + str(count) + ':')
27
man = input('Enter the manufacturer: ')
28
mod = input('Enter the model number: ')
29
retail = float(input('Enter the retail price: '))
30
print()
31

32
# Create a new CellPhone object in memory and
33
# assign it to the phone variable.
34
phone = cellphone.CellPhone(man, mod, retail)
35

36
# Add the object to the list.
37
phone_list.append(phone)
38

39
# Return the list.
40
return phone_list
41

42
# The display_list function accepts a list containing
43
# CellPhone objects as an argument and displays the
44
# data stored in each object.
45

46
def display_list(phone_list):
47
for item in phone_list:
48
print(item.get_manufact())
49
print(item.get_model())
50
print(item.get_retail_price())
51
print()
52

53
# Call the main function.
54
main()
...
cellphone.py
...
 3
class cellphone:
 4

 5

12
# The set_manufact method accepts an argument for
13
# the phone's manufacturer.
14

15
def set_manufact(self, manufact):
16
self.__manufact = manufact
17

18
# The set_model method accepts an argument for
19
# the phone's model number.
20

21
def set_model(self, model):
22
self.__model = model
23

24
# The set_retail_price method accepts an argument
25
# for the phone's retail price.
26

27
def set_retail_price(self, price):
28
self.__retail_price = price
29

30
# The get_manufact method returns the
31
# phone's manufacturer.
32

33
def get_manufact(self):
34
return self.__manufact
35

36
# The get_model method returns the
37
# phone's model number.
38

39
def get_model(self):
40
return self.__model
41

42
# The get_retail_price method returns the
43
# phone's retail price.
44

45
def get_retail_price(self):
46
return self.__retail_price





# Passing Objects as Arguments

def show_coin_status(coin_obj):
     print('This side of the coin is up:', coin_obj.get_sideup())

my_coin = coin.Coin()
show_coin_status(my_coin)


# When you pass a object as an argument, the thing that is passed into the parameter variable is a reference to the object. As a result, the function or method that receives the object as an argument has access to the actual object. For example, look at the following flip method:

def flip(coin_obj):
     coin_obj.toss()

# This method accepts a Coin object as an argument, and it calls the object’s toss method.

1
# This program passes a Coin object as
 2
# an argument to a function.
 3
import coin
 4

 5
# main function
 6
def main():
 7
# Create a Coin object.
 8
my_coin = coin.Coin()
 9

10
# This will display 'Heads'.
11
print(my_coin.get_sideup())
12

13
# Pass the object to the flip function.
14
flip(my_coin)
15

16
# This might display 'Heads', or it might
17
# display 'Tails'.
18
print(my_coin.get_sideup())
19

20
# The flip function flips a coin.
21
def flip(coin_obj):
22
coin_obj.toss()
23

24
# Call the main function.
25
main()

...

coin.py

...

6
class Coin:
7

8
# The __init__ method initializes the
9
# __sideup data attribute with 'Heads'.
10

11
def __init__(self):
12
self.__sideup = 'Heads'
13

14
# The toss method generates a random number
15
# in the range of 0 through 1. If the number
16
# is 0, then sideup is set to 'Heads'.
17
# Otherwise, sideup is set to 'Tails'.
18

19
def toss(self):
20
if random.randint(0, 1) == 0:
21
self.__sideup = 'Heads'
22
else:
23
self.__sideup = 'Tails'
24

25
# The get_sideup method returns the value
26
# referenced by sideup.
27

28
def get_sideup(self):
29
return self.__sideup





# Pickling Your Own Objects
1
# This program pickles CellPhone objects.
 2
import pickle
 3
import cellphone
 4

 5
# Constant for the filename.
 6
FILENAME = 'cellphones.dat'
 7

 8
def main():
 9
# Initialize a variable to control the loop.
10
again = 'y'
11

12
# Open a file.
13
output_file = open(FILENAME, 'wb')
14

15
# Get data from the user.
16
while again.lower() == 'y':
17
# Get cell phone data.
18
man = input('Enter the manufacturer: ')
19
mod = input('Enter the model number: ')
20
retail = float(input('Enter the retail price: '))
21

22
# Create a CellPhone object.
23
phone = cellphone.CellPhone(man, mod, retail)
24

25
# Pickle the object and write it to the file.
26
pickle.dump(phone, output_file)
27

28
# Get more cell phone data?
29
again = input('Enter more phone data? (y/n): ')
30

31
# Close the file.
32
output_file.close()
33
print('The data was written to', FILENAME)
34

35
# Call the main function.
36
main()
...
cellphone.py
...
 3
class CellPhone:
 4

 5
# The __init__ method initializes the attributes.
 6

 7
def __init__(self, manufact, model, price):
 8
self.__manufact = manufact
 9
self.__model = model
10
self.__retail_price = price



 1
# This program pickles CellPhone objects.
 2
import pickle
 3
import cellphone
 4

 5
# Constant for the filename.
 6
FILENAME = 'cellphones.dat'
 7

 8
def main():
 9
# Initialize a variable to control the loop.
10
again = 'y'
11

12
# Open a file.
13
output_file = open(FILENAME, 'wb')
14

15
# Get data from the user.
16
while again.lower() == 'y':
17
# Get cell phone data.
18
man = input('Enter the manufacturer: ')
19
mod = input('Enter the model number: ')
20
retail = float(input('Enter the retail price: '))
21

22
# Create a CellPhone object.
23
phone = cellphone.CellPhone(man, mod, retail)
24

25
# Pickle the object and write it to the file.
26
pickle.dump(phone, output_file)
27

28
# Get more cell phone data?
29
again = input('Enter more phone data? (y/n): ')
30

31
# Close the file.
32
output_file.close()
33
print('The data was written to', FILENAME)
34

35
# Call the main function.
36
main()
...
cellphone.py
...
 3
class CellPhone:
 4

 5
# The __init__ method initializes the attributes.
 6

 7
def __init__(self, manufact, model, price):
 8
self.__manufact = manufact
 9
self.__model = model
10
self.__retail_price = price








# unpickle_cellphone.py
1
# This program unpickles CellPhone objects.
 2
import pickle
 3
import cellphone
 4

 5
# Constant for the filename.
 6
FILENAME = 'cellphones.dat'
 7

 8
def main():
 9
end_of_file = False # To indicate end of file
10

11
# Open the file.
12
input_file = open(FILENAME, 'rb')
13

14
# Read to the end of the file.
15
while not end_of_file:
16
try:
17
# Unpickle the next object.
18
phone = pickle.load(input_file)
19

20
# Display the cell phone data.
21
display_data(phone)
22
except EOFError:
23
# Set the flag to indicate the end
24
# of the file has been reached.
25
end_of_file =True
26

27
# Close the file.
28
input_file.close()
29

30
# The display_data function displays the data
31
# from the CellPhone object passed as an argument.
32
def display_data(phone):
33
print('Manufacturer:', phone.get_manufact())
34
print('Model Number:', phone.get_model())
35
print('Retail Price: $', \
36
    format(phone.get_retail_price(), ',.2f'), \
37
    sep='')
38
print()
39

40
# Call the main function.
41
main()

...

cellphone.py

...

3
class CellPhone:
4

5
# The __init__ method initializes the attributes.
6

7
def __init__(self, manufact, model, price):
8
self.__manufact = manufact
9
self.__model = model
10
self.__retail_price = price
11

12
# The set_manufact method accepts an argument for
13
# the phone's manufacturer.
14

15
def set_manufact(self, manufact):
16
self.__manufact = manufact
17

18
# The set_model method accepts an argument for
19
# the phone's model number.
20

21
def set_model(self, model):
22
self.__model = model
23

24
# The set_retail_price method accepts an argument
25
# for the phone's retail price.
26

27
def set_retail_price(self, price):
28
self.__retail_price = price
29

30
# The get_manufact method returns the
31
# phone's manufacturer.
32

33
def get_manufact(self):
34
return self.__manufact
35

36
# The get_model method returns the
37
# phone's model number.
38

39
def get_model(self):
40
return self.__model
41

42
# The get_retail_price method returns the
43
# phone's retail price.
44

45
def get_retail_price(self):
46
return self.__retail_price








# Storing Objects in a Dictionary
1
# The Contact class holds contact information.
 2

 3
class Contact:
 4
# The __init__ method initializes the attributes.
 5
def __init__(self, name, phone, email):
 6
self.__name = name
 7
self.__phone = phone
 8
self.__email = email
 9

10
# The set_name method sets the name attribute.
11
def set_name(self, name):
12
self.__name = name
13

14
# The set_phone method sets the phone attribute.
15
def set_phone(self, phone):
16
self.__phone = phone
17

18
# The set_email method sets the email attribute.
19
def set_email(self, email):
20
self.__email = email
21

22
# The get_name method returns the name attribute.
23
def get_name(self):
24
return self.__name
25

26
# The get_phone method returns the phone attribute.
27
def get_phone(self):
28
return self.__phone
29

30
# The get_email method returns the email attribute.
31
def get_email(self):
32
return self.__email
33

34
# The __str__ method returns the object's state
35
# as a string.
36
def __str__(self):
37
return "Name: " + self.__name + \
38
    "\nPhone: " + self.__phone + \
39
    "\nEmail: " + self.__email


# he program displays a menu that allows the user to perform any of the following operations:

Look up a contact in the dictionary
Add a new contact to the dictionary
Change an existing contact in the dictionary
Delete a contact from the dictionary
Quit the program
Additionally, the program automatically pickles the dictionary and saves it to a file when the user quits the program.

1
# This program manages contacts.
 2
import contact
 3
import pickle
 4

 5
# Global constants for menu choices
 6
LOOK_UP = 1
 7
ADD = 2
 8
CHANGE = 3
 9
DELETE = 4
10
QUIT = 5
11

12
# Global constant for the filename
13
FILENAME = 'contacts.dat'
14

15
# main function
16
def main():
17
# Load the existing contact dictionary and
18
# assign it to mycontacts.
19
mycontacts = load_contacts()
20

21
# Initialize a variable for the user's choice.
22
choice = 0
23

24
# Process menu selections until the user
25
# wants to quit the program.
26
while choice != QUIT:
27
# Get the user's menu choice.
28
choice = get_menu_choice()
29

30
# Process the choice.
31
if choice == LOOK_UP:
32
look_up(mycontacts)
33
elif choice == ADD:
34
add(mycontacts)
35
elif choice == CHANGE:
36
change(mycontacts)
37
elif choice == DELETE:
38
delete(mycontacts)
39

40
# Save the mycontacts dictionary to a file.
41
save_contacts(mycontacts)
42

43
def load_contacts():
44
try:
45
# Open the contacts.dat file.
46
input_file = open(FILENAME, 'rb')
47

48
# Unpickle the dictionary.
49
contact_dct = pickle.load(input_file)
50

51
# Close the phone_inventory.dat file.
52
input_file.close()
53
except IOError:
54
# Could not open the file, so create
55
# an empty dictionary.
56
contact_dct = {}
57

58
# Return the dictionary.
59
return contact_dct
60

61
# The get_menu_choice function displays the menu
62
# and gets a validated choice from the user.
63
def get_menu_choice():
64
print()
65
print('Menu')
66
print('---------------------------')
67
print('1. Look up a contact')
68
print('2. Add a new contact')
69
print('3. Change an existing contact')
70
print('4. Delete a contact')
71
print('5. Quit the program')
72
print()
73

74
# Get the user's choice.
75
choice = int(input('Enter your choice: '))
76

77
# Validate the choice.
78
while choice < LOOK_UP or choice > QUIT:
79
choice = int(input('Enter a valid choice: '))
80

81
# return the user's choice.
82
return choice
83

84
# The look_up function looks up an item in the
85
# specified dictionary.
86
def look_up(mycontacts):
87
# Get a name to look up.
88
name = input('Enter a name: ')
89

90
# Look it up in the dictionary.
91
print(mycontacts.get(name, 'That name is not found.'))
92

93
# The add function adds a new entry into the
94
# specified dictionary.
95
def add(mycontacts):
96
# Get the contact info.
97
name = input('Name: ')
98
phone = input('Phone: ')
99
email = input('Email: ')
100

101
# Create a Contact object named entry.
102
entry = contact.Contact(name, phone, email)
103

104
# If the name does not exist in the dictionary,
105
# add it as a key with the entry object as the
106
# associated value.
107
if name not in mycontacts:
108
mycontacts[name] = entry
109
print('The entry has been added.')
110
else:
111
print('That name already exists.')
112

113
# The change function changes an existing
114
# entry in the specified dictionary.
115
def change(mycontacts):
116
# Get a name to look up.
117
name = input('Enter a name: ')
118

119
if name in mycontacts:
120
# Get a new phone number.
121
phone = input('Enter the new phone number: ')
122

123
# Get a new email address.
124
email = input('Enter the new email address: ')
125

126
# Create a contact object named entry.
127
entry = contact.Contact(name, phone, email)
128

129
# Update the entry.
130
mycontacts[name] = entry
131
print('Information updated.')
132
else:
133
print('That name is not found.')
134

135
# The delete function deletes an entry from the
136
# specified dictionary.
137
def delete(mycontacts):
138
# Get a name to look up.
139
name = input('Enter a name: ')
140

141
# If the name is found, delete the entry.
142
if name in mycontacts:
143
del mycontacts[name]
144
print('Entry deleted.')
145
else:
146
print('That name is not found.')
147

148
# The save_contacts funtion pickles the specified
149
# object and saves it to the contacts file.
150
def save_contacts(mycontacts):
151
# Open the file for writing.
152
output_file = open(FILENAME, 'wb')
153

154
# Pickle the dictionary and save it.
155
pickle.dump(mycontacts, output_file)
156

157
# Close the file.
158
output_file.close()
159

160
# Call the main function.
161
main()
162

163
# The Contact class holds contact information.
164

165
class Contact:
166
# The __init__ method initializes the attributes.
167
def __init__(self, name, phone, email):
168
self.__name = name
169
self.__phone = phone
170
self.__email = email
171

172
# The set_name method sets the name attribute.
173
def set_name(self, name):
174
self.__name = name
175

176
# The set_phone method sets the phone attribute.
177
def set_phone(self, phone):
178
self.__phone = phone
179

180
# The set_email method sets the email attribute.
181
def set_email(self, email):
182
self.__email = email
183

184
# The get_name method returns the name attribute.
185
def get_name(self):
186
return self.__name
187

188
# The get_phone method returns the phone attribute.
189
def get_phone(self):
190
return self.__phone
191

192
# The get_email method returns the email attribute.
193
def get_email(self):
194
return self.__email
195

196
# The __str__ method returns the object's state
197
# as a string.
198
def __str__(self):
199
return "Name: " + self.__name + \
200
"\nPhone: " + self.__phone + \
201
"\nEmail: " + self.__email




































