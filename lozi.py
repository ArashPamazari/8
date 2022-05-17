def lozi(rows):
	star = 0
	for i in range(1, rows + 1):
		for j in range (1, (rows - i) + 1):
			print(end = " ")
		while star != (2 * i - 1):
			print("*", end = "")
			star = star + 1
		star = 0
		print()

	space = 1
	star = 1

	for i in range(1, rows):
		for j in range (1, space + 1):
			print(end = " ")
		space = space + 1
		while star <= (2 * (rows - i) - 1):
			print("*", end = "")
			star = star + 1
		star = 1
		print()

rows = 5
lozi(rows)
