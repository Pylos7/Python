"""
Name: Nestor Ingles Jr
Course:  CSC - 121
Assignment:  Lesson 2 Lab - Question 1
"""
# Getting date information from user
month = int(input('Enter month (numeric):'))
day = int(input('Enter day:'))
year = int(input('Enter two digit year:'))

# Testing for magic
if month * day == year:
    print('This date is magic!')
else:
    print('This date is not magic') # Revel had this line with a period at the end as an answer
