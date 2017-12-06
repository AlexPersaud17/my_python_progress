def main():
	start_str = "NAISNIENLGELTETWEORRSD"
	crossed_chars = []
	remaining_chars = []
	index = 0
	for index in range(len(start_str)):
		if index % 2 == 0:
			crossed_chars.append(start_str[index])
		else:
			remaining_chars.append(start_str[index])
	print("\nStarting word:", start_str)
	print("Crossed-out letters:", "".join(crossed_chars))
	print("Remaining letters:", "".join(remaining_chars))

main()
