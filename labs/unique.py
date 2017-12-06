def main():
	xtuple = eval(input("Provide the values to test (including duplicates): "))
	uniq_vals = []
	for item in xtuple:
		if item not in uniq_vals:
			uniq_vals.append(item)

	print("There are", len(uniq_vals), "unique values in the tuple provided.")
	print("The unique values are:", uniq_vals)

main()
