# This program determines if the given year is a leap year or not

# def checkYear() :
#   year = eval(input("Enter a year to test: "))
#   if year % 4 == 0 :
#     if year % 400 == 0 :
#       print(year, "is a leap year.")
#     elif year % 100 == 0 :
#       print(year, "is not a leap year.")
#     else :
#       print(year, "is a leap year.")
#   else :
#     print(year, "is not a leap year.")

#   goAgain = input("Enter 'y' to test another year, otherwise, enter any other key: ")
#   if goAgain == "y" or goAgain == "Y" :
#     checkYear()

# checkYear()

# ******************************************
# ***********Changed code after*************
# ********we discussed while loops**********
# ******************************************

go_again = True;
while go_again :
  year = eval(input("Enter a year to test: "))
  if year % 4 == 0 :
    if year % 400 == 0 :
      print(year, "is a leap year.")
    elif year % 100 == 0 :
      print(year, "is not a leap year.")
    else :
      print(year, "is a leap year.")
  else :
    print(year, "is not a leap year.")

  another_test = input("Enter 'y' to test another year, otherwise, enter any other key: ")
  if another_test != "y" and another_test != "Y" :
    go_again = False