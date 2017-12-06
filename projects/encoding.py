#This program converts words from a text file to their ASCII translation
def translate_to_ASCII():
  infile = open("smalldictionary.txt")
  dict_words = infile.readlines()
  infile.close()

  words_to_ascii = []

  for word in dict_words:
    ascii_eq = []
    for letter in word.lower().rstrip("\n"):
      ascii_eq.append(str(ord(letter)))
    words_to_ascii.append(" ".join(ascii_eq) + "\n")

  outfile = open("encryptedwords.txt", "w")
  outfile.writelines(words_to_ascii)
  outfile.close()

translate_to_ASCII()