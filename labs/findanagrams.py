def letter_sorted_string(a_string):
  return "".join(sorted(a_string))


def main():
  print(letter_sorted_string(input("Please enter a string: ")))

main()