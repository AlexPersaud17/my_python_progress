#This program determine if the word given is an anagram.
def read_from_file():
  infile = open("encryptedwords.txt")
  encrypted_words = infile.readlines()
  infile.close()
  return encrypted_words

def decrypt(encrypted_words):
  dict_words = []
  for encrypted in encrypted_words:
    decrypted_word = ""
    for code in encrypted.split(" "):
      decrypted_word += chr(int(code))
    dict_words.append(decrypted_word)
  return dict_words

def sort_dict_words(dict_words):
  sorted_dict_words = {}
  for word in dict_words:
    sorted_dict_words[word] = "".join(sorted(word))
  return sorted_dict_words

def letter_sorted_string(a_string):
  return "".join(sorted(a_string))

def match_finder(sorted_user_input, user_input, dict_values, dict_keys):
  matches = []
  index = 0
  for word in dict_values:
    if sorted_user_input == word and user_input != dict_keys[index]:
      matches.append(dict_keys[index])
    index += 1
  return matches

def main(user_input):
  sorted_user_input = letter_sorted_string(user_input)
  decrypted_words = decrypt(read_from_file())
  sorted_dict_words = sort_dict_words(decrypted_words)

  dict_keys = list(sorted_dict_words.keys())
  dict_values = list(sorted_dict_words.values())

  if sorted_user_input in dict_values:
    matches = match_finder(sorted_user_input, user_input, dict_values, dict_keys)
    print("Found " + str(len(matches)) + " anagram(s) for '" + user_input + "': ", end = "")
    for index in range(len(matches)-1):
      print(matches[index], end = ", ")
    print(matches[-1])
  else:
    print("No anagrams found for '" + user_input + "'.")


def runner():
  print("Welcome to Anagram Finder 1.0")
  print("Enter nothing i.e. '' to quit the program.")

  run_program = True
  while run_program:
    user_input = input("\nEnter the word to test for anagrams in our database: ")
    if user_input != "":
      main(user_input)
    else:
      run_program = False
  
  print("\nThank you for using Anagram Finder 1.0")

runner()