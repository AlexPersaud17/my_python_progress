import random
def main():
	rolled_num1 = random.randint(1, 6)
	rolled_num2 = random.randint(1, 6)
	while rolled_num1 != rolled_num2:
		print("Your rolled a", rolled_num1, "and a", rolled_num2)
		rolled_num1 = random.randint(1, 6)
		rolled_num2 = random.randint(1, 6)
	print("Congratulations, you rolled two", rolled_num1 ,"'s!")


main()
