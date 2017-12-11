class RetailItem:
  def __init__(self, description, inventory, price):
    self.description = description
    self.inventory = inventory
    self.price = price

def print_menu():
  print('''\nMenu
--------------------
1. Jacket
2. Designer Jeans
3. Shirt''')

def take_order(cart, store):
  if (store[1].inventory - cart.get(1, 0) + store[2].inventory - cart.get(2, 0) + store[3].inventory - cart.get(3, 0)) != 0:
    user_purchase = input("\nEnter the menu number of the item you would like to purchase: ")
    while not user_purchase.isdigit() or not(1<=eval(user_purchase)<=3):
      print("Please enter a number from 1-3.")
      user_purchase = input("Enter the menu number of the item you would like to purchase: ")
    user_purchase = eval(user_purchase)

    if store[user_purchase].inventory - cart.get(user_purchase, 0) > 0:
      user_quantity = input("How many {}s would you like? : ".format(store[user_purchase].description))
      while not user_quantity.isdigit() or not(1<=eval(user_quantity)<=store[user_purchase].inventory - cart.get(user_purchase, 0)):
        print("\nPlease enter a positive number below {}.".format(store[user_purchase].inventory - cart.get(user_purchase, 0) + 1))
        user_quantity = input("How many {}'s would you like? : ".format(store[user_purchase].description))
      user_quantity = eval(user_quantity)

      cart[user_purchase] = cart.get(user_purchase, 0) + user_quantity
      print("Added {} {}s to your shopping cart.".format(user_quantity, store[user_purchase].description))

    else:
      print("\nSorry, we are out of {}s.".format(store[user_purchase].description))
      return True

  else:
    print("We have no more inventory in the entire store!")

  checkout = input("\nAre you ready to checkout? (y/n): ")
  while checkout.lower() not in ['y', 'n']:
    checkout = input("Please say 'y' or 'n': ")

  if checkout.lower() == "y":
    return False
  else:
    return True

def checkout(cart, store):
  print("\nYour Shopping Cart")
  total = 0.0
  for item, quantity in cart.items():
    print("{} x {}(s)".format(quantity, store[item].description))
    total += store[item].price * quantity
  print("Your total comes to ${}, have a great day.".format(round(total, 2)))

def main():
  item1 = RetailItem("Jacket", 12, 159.99)
  item2 = RetailItem("Designer Jean", 40, 149.99)
  item3 = RetailItem("Shirt", 20, 79.00)

  store = {1:item1, 2:item2, 3:item3}
  cart = {}

  ordering = True
  while ordering:
    print_menu()
    ordering = take_order(cart, store)

  checkout(cart, store)

main()