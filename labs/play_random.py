import random

def main():
	user_range = eval(input("Give me a positive integer and I will find your \"lucky number\" in this range: "))
	lucky_num = random.randint(1, user_range)
	print("your lucky number is:", lucky_num)
	print("Take a chance and bet on it!")
	
main()
