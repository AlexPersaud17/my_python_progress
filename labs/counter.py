import random

def main():	
	even_count = 0
	odd_count = 0
	for count in range(100):
		num = random.randint(1, 100)
		if num % 2 == 0:
			even_count += 1
		else:
			odd_count += 1
	print("Out of 100 random numbers,", odd_count, "were odd, and", even_count, "were even.")
		


main()
