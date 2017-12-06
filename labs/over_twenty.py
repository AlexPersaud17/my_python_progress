import random
def main():
	ages = []
	count = 1
	over_twenty = 0
	while count <= 10:
		new_age = random.randint(10, 40)
		ages.append(new_age)
		if new_age > 20:
			over_twenty += 1
		count += 1

	print("The group of ages:", ages)
	print("There were", over_twenty, "people over twenty!")


main()
