min = int(input("введите стартовое число"))
max = int(input("введите финишное число"))

counter = 0
while min != max + 1:
	if min % 2:
		print(min)
	min += 1
	counter += 1
	if counter > 999:
		break