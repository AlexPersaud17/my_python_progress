def main():
	lines = []
	i = 0
	my_file = open("story.txt", "r")

	line = my_file.readline()
	
	while line != "":
		lines.append(line)
		line = my_file.readline()

	my_file.close()


	lines.reverse()

	my_file = open("story.txt", "w")
	for xline in lines:
		my_file.write(xline)
	my_file.close()
	
	

main()
