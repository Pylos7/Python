"""
Name: Nestor Ingles Jr
Course:  CSC - 121
Assignment:  Practice Exercise 3.3B: Using while to Keep a Program Running
"""
# Getting number from user to print weekday
n1 = int(input('Enter a number between 1 and 7: '))
wd = 'weekDay'

# If statement testing input and assigning week day to wd
if n1 < 1 or n1 > 7:
    print('Incorrect input: Please restart program and enter a value 1 - 7')
elif n1 == 1:
    wd = 'Monday'
elif n1 == 2:
    wd = 'Tuesday'
elif n1 == 3:
    wd = 'Wednesday'
elif n1 == 4:
    wd = 'Thursday'
elif n1 == 5:
    wd = 'Friday'
elif n1 == 6:
    wd = 'Saturday'
else:
    wd = 'Sunday'

# Printing weekday
print('It is ', wd)
