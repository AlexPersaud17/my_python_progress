import random
def main():
	# hangman_str = input("Enter your secret phrase: ").lower()
	hangman_strs = ["I love python", "Hello, world!", "Programming is FUN!"]
	random_str = random.randint(1, len(hangman_strs)) - 1
	hangman_str = hangman_strs[random_str].lower()

	guessed_str = []
	guesses = []
	bodyparts = ["head", "nose", "left ear", "right ear", "left eye", "right eye", "mouth", "neck", "left arm", "right arm", "torso", "left leg", "right leg"]
	body_i = 0
	loser = False

	for l in hangman_str:
		if l.isalpha():
			guessed_str.append("_ ")
		else:
			guessed_str.append(l)
	
	while "_ " in guessed_str and not loser:
		print("\n", "".join(guessed_str))
		guess = input("\nPlease enter one letter: ")
		while not guess.isalpha() or len(guess) != 1:
			guess = input("\nPlease enter one letter: ")
		
		if guess in guesses:
			print("You guessed that letter already!")

		else:
			guesses.append(guess)

			if guess in hangman_str:
				print("Found", hangman_str.count(guess), "occurence(s) of the letter", guess, "in the sentence!")
				
				while guess in hangman_str:
					guess_index = hangman_str.find(guess)
					guessed_str[guess_index] = guess
					
					hangman_str = list(hangman_str)
					hangman_str[guess_index] = "_"
					hangman_str = "".join(hangman_str)

			else:
				print("Sorry, that letter is not in the sentence.")
				print("You now have a", bodyparts[body_i].upper(), "added to the hangman.")
				if body_i == len(bodyparts)-1:
					loser = True
					continue
				else:
					body_i += 1

			print("\nLetters used so far: ", end = "")
			for g in range(len(guesses)-1):
  				print(guesses[g], end=", ")
			print(guesses[-1])

	if not loser:
		print("\nYou win! The hangman sentence is:", "".join(guessed_str))
	else:
		print("\nSorry, you lose!")
		print('''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
Thanks for playing!
		''')


main()
