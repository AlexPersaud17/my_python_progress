def main():
	print("Enter a number from the menu to obtain a fact about the United States or to exit the program.")
	print("\t1. Capital")
	print("\t2. National Bird")
	print("\t3. National Flower")
	print("\t4. Quit")

	another_fact = True
	while another_fact:
		user_input = eval(input("Make a selection from the menu: "))
		if(user_input == 1):
			print("Washington D.C. is the capital.")
		elif(user_input == 2):
			print("The American Bald Eagle is the national bird.")
		elif(user_input == 3):
			print("The Rose is the national flower.")
		elif(user_input == 4):
			print("Goodbye!")
			another_fact = False
		else:
			print("Invalid option.")
	



main()
