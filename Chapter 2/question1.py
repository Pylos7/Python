numCookies = int(input("Enter number of cookies:"))

x = str(format(1.5*numCookies/48, '.2f'))
y = str(format(numCookies/48, '.2f'))
z = str(format(2.75*numCookies/48, '.2f'))

print('You need ' + x + ' cups of sugar, ' + y + ' cups of butter, and ' + z + ' cups of flour.')
