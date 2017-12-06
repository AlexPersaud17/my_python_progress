# This program computes various operatios based on the user input
x, y = eval(input("Enter two numbers: "))
operation = input("Enter the operation: ")
result = ""

if operation == "+" or operation == "a" :
  operation = "+"
  result = x + y

elif operation == "-" or operation == "s" :
  operation = "-"
  result = x - y

elif operation == "*" or operation == "m" :
  operation = "*"
  result = x * y

elif operation == "/" or operation == "d" :
  if y != 0 :
    operation = "/"
    result = x / y
  else :
    print("Cannot compute! The divisor operand should not be zero!")

elif operation == "%" or operation == "r" :
  operation = "%"
  result = x % y

elif operation == "^" or operation == "p" :
  operation = "^"
  result = x ** y

if result != "":
  print("Result: ", x, operation, y," = ", result, sep="")
else :
  print("Please enter a valid operation!")