#This program displays memorable quotes from memorable movies.
import random

def load_database():
  filename = input("Enter the name of the file to load: ")
  try:
    infile = open(filename)
  except:
    print("Couldn't find a file with that name. Program will use the 'movie_quotes.txt' file instead.")
    filename = "movie_quotes.txt"
    infile = open(filename)

  movie_titles_and_quotes = infile.readlines()
  infile.close()

  quotes_dict = {}
  for title_quote in movie_titles_and_quotes:
    quotes_dict[title_quote.split("--")[0].strip().lower()] = quotes_dict.get(title_quote.split("--")[0].strip().lower(), []) + [title_quote.split("--")[1]]

  return quotes_dict, filename

def rewrite_to_database(quotes_dict, filename):
  outfile = open(filename, "w")
  for title, quotes in quotes_dict.items():
    for quote in quotes:
      outfile.write("{} -- {}\n".format(title.title(), quote.strip().rstrip("\n")))
  outfile.close()

def print_menu(quotes_dict, filename):
  print('''\nChoose one of the following options:
  1. Print all movie-titles in the database.
  2. Print all movie-quotes in the database.
  3. Print both movie-titles and relevant quotes from the database.
  4. Print the quote for one of our movies.
  5. Add a new quote in the database (You have to provide the movie title too).
  6. Display a random quote from the database.
  7. Remove a movie from the database.
  8. Quit.''')

  user_menu_choice = input("\nEnter your choice: ")
  while not user_menu_choice.isdigit() or not (1<=eval(user_menu_choice)<=8):
    print("Invalid option.")
    user_menu_choice = input("\nEnter your choice: ")
  print()

  run_program = True

  user_menu_choice = eval(user_menu_choice)
  if user_menu_choice == 1:
    print_movies(quotes_dict)

  elif user_menu_choice == 2:
    print_quotes(quotes_dict)

  elif user_menu_choice == 3:
    print_all(quotes_dict)

  elif user_menu_choice == 4:
    print_the_quote(quotes_dict)

  elif user_menu_choice == 5:
    quotes_dict = add_quote(quotes_dict, filename)

  elif user_menu_choice == 6:
    display_random_quote(quotes_dict)

  elif user_menu_choice == 7:
    remove_movie(quotes_dict)

  elif user_menu_choice == 8:
    quit(quotes_dict, filename)
    run_program = False

  return run_program

def print_movies(quotes_dict):
  print("\nMOVIES")
  for title in quotes_dict.keys():
    print(title.title())

def print_quotes(quotes_dict):
  print("\nQUOTES")
  for quotes in quotes_dict.values():
    print()
    for quote in quotes:
      print("--\"" + quote.strip().rstrip("\n") + "\"")

def print_all(quotes_dict):
  print("\nMOVIES & QUOTES")
  for title, quotes in quotes_dict.items():
    print()
    print(title.title())
    for quote in quotes:
      print("--\"" + quote.strip().rstrip("\n") + "\"")

def print_the_quote(quotes_dict):
  user_movie_name = input("Search for the name of a movie: ")
  while user_movie_name == "":
    user_movie_name = input("Search for the name of a movie: ")

  try:
    for quote in quotes_dict[user_movie_name]:
      print("--\"" + quote.strip().rstrip("\n") + "\"")

  except:
    print("That movie is not in our database.")

def add_quote(quotes_dict, filename):
  user_new_movie = input("Please provide a movie title: ")
  while user_new_movie == "":
    user_new_movie = input("Please provide a movie title: ")

  user_new_quotes = []
  new_quote = input("Quote(s): (Press ENTER when done) ")
  while new_quote != "":
    user_new_quotes.append(new_quote)
    new_quote = input()

  quotes_dict[user_new_movie.lower()] = quotes_dict.get(user_new_movie.lower(), []) + user_new_quotes
  
  return quotes_dict

def display_random_quote(quotes_dict):
  random_title = random.choice(list(quotes_dict.keys()))
  print("Movie:", random_title.title())
  print("Quote: \"" + random.choice(quotes_dict[random_title]).strip().rstrip("\n") + "\"")

def remove_movie(quotes_dict):
  user_remove_movie = input("Enter the name of the movie you would like to remove: ")
  while user_remove_movie == "":
    user_remove_movie = input("Enter the name of the movie you would like to remove: ")

  try:
    del quotes_dict[user_remove_movie.lower()]
    print("\"" + user_remove_movie.title() + "\" has been removed.")
  except:
    print("That movie is not in our database.")

def quit(quotes_dict, filename):
  user_save_changes = input("Would you like to save any changes you made to the database?: ")
  if user_save_changes.lower() in ["yes", "y", "sure", "yeah"]:
    print("Great! Our database has been updated.")
    rewrite_to_database(quotes_dict, filename)
  else:
    print("Ok! Undoing all changes made.")

def main():
  print("Welcome to OMGdb Movie Quotes!")
  global quotes_dict
  quotes_dict, filename = load_database()

  run_program = True
  while run_program:
    run_program = print_menu(quotes_dict, filename)

  print("\nThank you for using OMGdb Movie Quotes!")

main()