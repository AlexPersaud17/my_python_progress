#This program plays Hangman with the user!
import random
def main():
  
  secrets = []
  
  phrases_file = open("hangmanphrases.txt", "r")
  line = phrases_file.readline()
  while line != "":
    secrets.append(line.rstrip("\n"))
    line = phrases_file.readline()
  phrases_file.close()

  print("Let's play Hangman!")

  go_again = True
  while go_again:
    
    random_str = random.randint(1, len(secrets)) - 1
    hangman_str = secrets[random_str].lower()
    
    guessed_list = []
    guesses = []

    bodyparts = ["head", "nose", "left ear", "right ear", "left eye", "right eye", "mouth", "neck", "left arm", "right arm", "torso", "left leg", "right leg"]
    body_i = 0
    loser = False

    for l in hangman_str:
      if l.isalpha():
        guessed_list.append("_ ")
      else:
        guessed_list.append(l)

    hangman_chars = guessed_list.count("_ ")

    while "_ " in guessed_list and not loser:
      print("\nThe secret sentence is:", "".join(guessed_list))

      user_solve = ""
      if "".join(guessed_list).count("_ ") / hangman_chars <= 0.5:
        user_solve = input("\nWould you like to solve? (yes/no): ")

      if user_solve.lower() in ["yes", "y", "yeah", "yes!", "ok", "okay", "pat, i'd like to solve!"]:
        user_full_guess = input("Please enter the full phrase!\n")

        without_punctuation = ""
        for ch in secrets[random_str]:
          if ch.isalpha() or ch == " ":
            without_punctuation += ch

        if user_full_guess.lower() == without_punctuation.lower():
          guessed_list = list(secrets[random_str].lower())

        else:
          loser = True
          
      else:
        guess = input("Please enter one letter: ")
        while not guess.isalpha() or len(guess) != 1:
          guess = input("Please enter one letter: ")
        
        if guess in guesses:
          print("You guessed that letter already!")

        else:
          guesses.append(guess)

          if guess in hangman_str:
            print("Found", hangman_str.count(guess), "occurence(s) of the letter", guess.upper(), "in the sentence!")
            
            while guess in hangman_str:
              guess_index = hangman_str.find(guess)
              guessed_list[guess_index] = secrets[random_str][guess_index]
              
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

          print("Letters used so far: ", end = "")
          for g in range(len(guesses)-1):
              print(guesses[g], end=", ")
          print(guesses[-1])

    if not loser:
      print("\nYou win! The hangman sentence is:", secrets[random_str])
    else:
      print("\nSorry, you lose! The hangman sentence is:", secrets[random_str])
    
    user_response = input("\nType 'again' to play again, otherwise, press anything else to exit: ")
    if user_response.lower() != "again":
      go_again = False

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