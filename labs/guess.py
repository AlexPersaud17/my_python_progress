import random
def main():
	upper_limit = 20
	lucky_num = random.randint(1, upper_limit)
	incorrect  = True
	while incorrect:
		user_guess = eval(input("Enter your guess: "))
		if user_guess < 1 or user_guess > upper_limit:
			print("Hint: it's a number between 1 and", upper_limit)
		elif user_guess < lucky_num:
			print("Too low!")
		elif user_guess > lucky_num:
			print("Too high!")
		else:
			incorrect = False
	print("Correct! You win!")


main()
