# This program calculates the approx. length of a snowboard needed for a rider of a certain height

def main():
	print("Enter your height")
	feet = eval(input("Feet: "))
	inches = eval(input("Inches: "))

	total_inches = feet * 12 + inches
	total_centimeters = total_inches * 2.54

	board_length = round(total_centimeters * .88)

	print("Suggested board length:", board_length, "cm")

main()
