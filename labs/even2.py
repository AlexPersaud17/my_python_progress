def main():
	upper_limit = eval(input("Declare an upper limit: "))
	print("Computations for thr first", upper_limit, "positive even numbers.")
	sum = 0
	count = 0
	i = 0
	while i <= upper_limit:
		sum += i
		count += 1
		i += 2
	average = sum / count
	print("Sum:", sum, "Average:", average)



main()
