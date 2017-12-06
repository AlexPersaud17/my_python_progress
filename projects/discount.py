#This program adds a discount to the users price based on its cost
price = eval(input("Enter an item price: "))

if 0 < price <= 30 :
  print("No discount, final price = $", price, sep="")
elif 30 < price <= 100 :
  print("10% discount, final price = $", price * .9, sep="")
elif price > 100 :
  print("20% discount, final price = $", price * .8, sep="")
else :
  print("Please try again with a non-negative value!")