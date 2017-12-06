# You need a different implementation of the function without using a dictionary

def determine_rank(years):
	rank_dict = {1: "Freshman", 2: "Sophomore", 3: "Junior", 4: "Senior"}
	if years in rank_dict:
		return rank_dict[years]
	else:
		return "Oops, something went wrong!"



def main():
	## Determine an admission fee based on age group.
	print("Enter how many years you are attending Hofstra ", end="")
	try:
		years = eval(input("(only full numbers): "))
	except:
		print("Oops, something went wrong!")
	else:
		print("Then you are ...", determine_rank(years) )       

main()
