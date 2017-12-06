def main() :
	while True :
		print("Find out the colors on the roulette wheel!")
		num = eval(input("Please enter a number from 0 to 36: "))
		if num == 0 :
			color = "Green"
		elif 1 <= num <= 10 :
			if num % 2 == 0 :
				color = "Black"
			else:
				color = "Red"
		elif 11 <= num <= 18 :
			if num % 2 == 0 :
				color = "Red"
			else:
				color = "Black"
		elif 19 <= num <= 28 :
			if num % 2 == 0 :
				color = "Black"
			else:
				color = "Red"
		elif 29 <= num <= 36 :
			if num % 2 == 0 :
				color = "Red"
			else:
				color = "Black"
		else:
			print("Error: Invalid input")
			go_again = input("Try another number? ")
			if go_again == "yes" :
				continue
			else :
				break
	
	
		print("Color:", color)
		break
		


main()
