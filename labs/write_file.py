def main():
	my_file = open("shopping_list.txt", "w")
	my_file.write("fruits: {}, {}, {}\n".format("apples", "bananas", "oranges"))
	my_file.write("dairy: {}, {}\n".format("yogurt", "milk"))
	my_file.write("desserts: {}\n".format("chocolate cake"))
	my_file.write("cleaning: {}, {}\n".format("fantastic scrubbing bubbles", "fabuloso"))

	my_file.close()


main()
