def main():
	upper_limit = eval(input("Declare an upper limit: "))
	print("Computations for thr first", upper_limit, "positive even numbers.")
	sum = 0
	count = 0
	for i in range(0, upper_limit + 1, 2):
		sum += i
		count += 1
	average = sum / count
	print("Sum:", sum, "Average:", average)
	
	
main()
