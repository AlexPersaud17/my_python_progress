#This program displays banking options to the user
def main():
  current_balance = 1000
  go_again = True

  print("\nOPTIONS:")
  print("1. Make a Deposit")
  print("2. Make a Withdrawal")
  print("3. Obtain Balance")
  print("4. Quit")

  while go_again :
    selection = input("\nMake a selection from the options menu: ")
    if selection.isdigit() :
      selection = eval(selection)

      if selection == 1 :
        deposit = input("Enter amount of deposit: $")
        while not deposit.isdigit():
          print("Invalid amount, please try again.")
          deposit = input("Enter amount of deposit: $")
        current_balance += eval(deposit)

      elif selection == 2 :
        withdrawal = input("Enter amount of withdrawal: $")
        while not withdrawal.isdigit():
          print("Invalid amount, please try again.")
          withdrawal = input("Enter amount of withdrawal: $")

        withdrawal = eval(withdrawal)
        if withdrawal > current_balance :
          print("Denied. Maximum withdrawal is $", current_balance, sep = "")
        else :
          current_balance -= withdrawal

      elif selection == 3 :
        print("Balance: $", current_balance, sep = "")
        
      elif selection == 4 :
        print("Thank you for using our bank.")
        go_again = False
      else :
        print("Invalid option.")
    else :
      print("Invalid option.")


main()