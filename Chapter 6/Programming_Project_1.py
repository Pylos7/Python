def main():
	total = 0.0
	count = 0

	file = open('numbers.txt','r')

	for line in file:
		number = float(line)
		count = count + 1
		total = total + number
		
	average = total / count
	print(average)

main()
