#This program is a dice rolling game
import random
def main():
  die_one = '''
   ______
  |      |
  |  ()  |
  |______|'''
  die_two = '''
   ______
  |()    |
  |      |
  |____()|'''
  die_three = '''
   ______
  |()    |
  |  ()  |
  |____()|'''
  die_four = '''
   ______
  |()  ()|
  |      |
  |()__()|'''
  die_five = '''
   ______
  |()  ()|
  |  ()  |
  |()__()|'''
  die_six = '''
   ______
  |()  ()|
  |()  ()|
  |()__()|'''
  ascii_arts = [die_one, die_two, die_three, die_four, die_five, die_six]


  print("\nTest Your Luck! Here are the rules:\n")
  print("1. You are going to roll two dice.")
  print("2. If you roll a 7 or 11 on that roll, you win!")
  print("3. However, if you roll a 2, 3, or 12, you lose.")
  print("4. If you roll any other number, you will keep rolling until:")
  print("\t-You hit the same number, in which case you win!")
  print("\t-You roll a 7, which in this case is an automatic loss.")
  print("\nGood luck!\n")

  lets_roll = input("Roll the dice? (y/n)\n")
  if lets_roll.lower() not in ["yes", "y", "yeah", "yes!", "ok", "okay", "sure"]:
    print("\nQuitting...")

  else:
    dice = [random.randint(1, 6), random.randint(1, 6)]
    throw = (sum(dice),)
    
    print(ascii_arts[dice[0]-1], ascii_arts[dice[1]-1])
    print("\nYou rolled a", throw[-1])


    if throw[0] in [7, 11]:
      print("\nYou win!")
    elif throw[0] in [2, 3, 12]:
      print("\nYou lose.")
    else:
      print("You need to roll another", throw[0], "to win!")

      lets_roll = input("\nRoll again? (y/n)\n")
      roll_again = True
      if lets_roll.lower() not in ["yes", "y", "yeah", "yes!", "ok", "okay", "sure"]:
        print("\nQuitting...")

      else:
        print("Rolling again...")
        dice = [random.randint(1, 6), random.randint(1, 6)]
        throw += (sum(dice),)

        while sum(dice) not in [throw[0], 7] and roll_again == True:
          print(ascii_arts[dice[0]-1], ascii_arts[dice[1]-1])
          print("\nYou rolled a", throw[-1])
          print("You need to roll another", throw[0], "to win!")
          lets_roll = input("\nRoll again? (y/n)\n")
          if lets_roll.lower() not in ["yes", "y", "yeah", "yes!", "ok", "okay", "sure"]:
            print("\nQuitting...")
            roll_again = False

          else:
            print("Rolling again...")
            dice = [random.randint(1, 6), random.randint(1, 6)]
            throw += (sum(dice),)

        if throw[-1] == 7:
          print(ascii_arts[dice[0]-1], ascii_arts[dice[1]-1])
          print("\nYou lose. You rolled a 7.")
        elif throw[-1] == throw[0]:
          print(ascii_arts[dice[0]-1], ascii_arts[dice[1]-1])
          print("\nYou rolled another ", throw[0], ", you win!", sep = "")

main()