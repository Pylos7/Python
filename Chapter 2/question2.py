maleNum = int(input('Enter number of males:'))
femaleNum = int(input('Enter number of females:'))
total = maleNum + femaleNum
malePercent = maleNum/total
femalePercent = femaleNum/total

print('Percent males: ' + format(malePercent, '.0%'))
print('Percent females: ' + format(femalePercent, '.0%'))
