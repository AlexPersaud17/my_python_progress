def main():
	num_col = eval(input("How many columns? "))
	for up in range(num_col):
		print(" " * (up), "#")
	for down in range(num_col-1, 0, -1):
		print(" " * (down-1), "#")

main()
