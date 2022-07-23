# Nestor Ingles Jr
# CSC 121 (Phyton)

n1 = int(input('Enter a number between 1 and 7: '))
wd = 'weekDay'
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

print('It is ', wd)
