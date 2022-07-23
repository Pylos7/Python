grades = input()
counter = 0
sum = 0

while grades != "stop":
	sum += int(grades)
	counter += 1
	grades = input()
print(sum/counter)
