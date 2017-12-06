# This method takes a two-digit number and switches the order

def main():
	original = 24
	tens_digit = original // 10
	ones_digit = original % 10
	original_reversed = ones_digit * 10 + tens_digit
	
	print("\nInitially, the two-digit number was:", original)
	print("The reversed number is:", original_reversed, end="\n\n")

main()

def three_digit():
	original = 617
	hundreds_digit = original // 100
	tens_digit = original % 100 // 10
	ones_digit = original % 100 % 10
	original_reversed = ones_digit * 100 + tens_digit * 10 + hundreds_digit

	print("Initially, the three-digit number was:", original)
	print("The reversed number is:", original_reversed, end="\n\n")

three_digit()


