# This program takes a cent value from the user and it outputs the least amount of coins needed to match
cents = eval(input("Enter amount of money in cents: "))
numQuarters = cents // 25

cents -= numQuarters * 25
numDimes = cents // 10

cents -= numDimes * 10
numNickels = cents // 5

cents -= numNickels * 5
numPennies = cents

print("The optimal change is:", numQuarters, "quarters,", numDimes, "dimes,", numNickels, "nickels, and", numPennies, "pennies.")