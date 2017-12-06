def main():
	infile = open("rosebowl.txt")
	team_wins = {}
	line = infile.readline().rstrip("\n")
	while line != "":
		if line in team_wins:
			team_wins[line] += 1
		else:
			team_wins[line] = 1

		line = infile.readline().rstrip("\n")

	infile.close()
	
	print("Teams with four or more wins in the Rose Bowl are:")
	
	for team in team_wins:
		if team_wins.get(team) >= 4:
			print(team, team_wins.get(team), sep = ": ")




main()
