def main():
	print("Minutes\t\tCalories Burned")
	for i in range(31):
		print("-", end="")
	print()
	for i in range(10, 31, 5):
		print(i, i*3.9, sep="\t\t")
	

main()
