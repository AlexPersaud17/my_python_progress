import random
def main():
	rolled_num = random.randint(1, 6)
	while rolled_num != 6:
		print("Your rolled a", rolled_num)
		rolled_num = random.randint(1, 6)
	print("Congratulations, you rolled a 6!")


main()
