#This program encrypts and decrypts user text
def main():
  print("\nStarting out with Cryptography!")
  go_again = True
  while go_again:
    print("\nChoose one of the three options (1-3) shown below:")
    print("\t1. Encrypt a message")
    print("\t2. Decrypt a message")
    print("\t3. Quit")
    option = input("Enter your choice: ")
    if option.isdigit() and 1<=eval(option)<=3:
      option = eval(option)

    if option == 1:
      plaintext = input("Plaintext message: ")
      while not plaintext.isalpha():
        print("Please only enter letters.")
        plaintext = input("Plaintext message: ")
      
      rotation = input("Size of rotation (1-25): ")
      while not rotation.isdigit() or not 1<=eval(rotation)<=25:
        print("Please use digits from 1-25.")
        rotation = input("Size of rotation (1-25): ")

      rotation = eval(rotation)
      ciphertext = ""
      for letter in plaintext:
        if letter.islower():
          if ord(letter) + rotation <= 122:
            ciphertext += chr(ord(letter) + rotation)
          else:
            ciphertext += chr((ord(letter) + rotation) - 26)
        else:
          if ord(letter) + rotation <= 90:
            ciphertext += chr(ord(letter) + rotation)
          else:
            ciphertext += chr((ord(letter) + rotation) - 26)
          

      print("Encrypted Message:", ciphertext)

    elif option == 2:
      ciphertext = input("Ciphertext message: ")
      while not ciphertext.isalpha():
        print("Please only enter letters.")
        ciphertext = input("Ciphertext message: ")

      rotation = input("Size of rotation (1-25): ")
      while not rotation.isdigit() or not 1<=eval(rotation)<=25:
        print("Please use digits from 1-25.")
        rotation = input("Size of rotation (1-25): ")

      rotation = eval(rotation)
      plaintext = ""
      for letter in ciphertext:
        if letter.islower():
          if ord(letter) - rotation >= 97:
            plaintext += chr(ord(letter) - rotation)
          else:
            plaintext += chr((ord(letter) - rotation) + 26)
        else:
          if ord(letter) - rotation >= 65:
            plaintext += chr(ord(letter) - rotation)
          else:
            plaintext += chr((ord(letter) - rotation) + 26)
          

      print("Decrypted Message:", plaintext)
          
    elif option == 3:
      go_again = False
      print("Hope you liked Cryptography, goodbye!")

    else:
      print("Valid options are: 1, 2 and 3. Try again.")


main()