def main() :	
	num = 0
	ITERATIONS = 6
	i = 1
	print("Number  Square")

	while i <= ITERATIONS:
		num += 1
		if num % 2 == 1 :
			num_sq = num**2
			print(num, num_sq, sep="\t")
			i += 1

main()
