# This program takes the pizza order of the user and calculates the total cost

def main():
	order_again = True
	print("\nWelcome to Lombardi's Pizza Place!\n")
	while order_again: 
		print("What size would you like?")
		print("\t1. small ($7.99)  2. medium ($14.99)  3. large ($18.99)\n")
	
		size_num = eval(input("Please enter 1 or 2 or 3 (for size): "))
		if size_num == 1 :
			size = "small"
			cost = 7.99
		elif size_num == 2 :
			size = "medium"
			cost = 14.99
		elif size_num == 3 :
			size = "large"
			cost = 18.99
		else :
			print("Invalid menu option!")
			try_again = input("Try again? ")
			if try_again == "yes" :
				continue
			else :
				break
	
		print("Ok, ", size, ", that is for $", cost, " each\n", sep="")
		quantity = eval(input("How many would you like? "))
		total = cost * quantity
		print("Your total is $", format(total, ".2f"), ".", sep="", end="\n\n")
	
		order_again = input("Would you like to make another order? ")
		if order_again != "yes" :
			order_again = False
			print("Thank you for choosing Lombardi's Pizza Place!")
	




main()
