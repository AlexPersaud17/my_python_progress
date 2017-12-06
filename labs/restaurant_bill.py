# This code calculates the total bill including tax and tip
def main():
	TIP_RATE = 0.18
	TAX_RATE = 0.09

	price = eval(input("Enter the \"net\" for food: "))

	tip = round((price * TIP_RATE), 2)
	print("Tip(18%): $", tip, sep="")

	tax = round((price * TAX_RATE), 2)
	print("Tax: $", tax, sep="")

	total = round((price + tip + tax), 2)
	print("Total: $", total, sep="")

	people = eval(input("Split this bill between how many people? "))
	per_person = round((total / people), 2)
	print("Each person pays $", per_person, sep="")

main()
