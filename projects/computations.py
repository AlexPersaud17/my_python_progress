# This program takes 3 numbers from the user and outputs the sum, average, product, and which numbers are odd

num1, num2, num3 = eval(input("Enter three different integers: "))

numSum = num1 + num2 + num3
print("Sum:", numSum)

numAverage = numSum / 3
print("Average:", numAverage)

numProduct = num1 * num2 * num3
print("Product:", numProduct)

if num1 % 2 == 1 and num2 % 2 == 1 and num3 % 2 == 1 :
  print("Odd numbers:", num1, num2, num3)
elif num1 % 2 == 1 and num2 % 2 == 1 and num3 % 2 != 1 :
  print("Odd numbers:", num1, num2)
elif num1 % 2 == 1 and num2 % 2 != 1 and num3 % 2 == 1 :
  print("Odd numbers:", num1, num3)
elif num1 % 2 != 1 and num2 % 2 == 1 and num3 % 2 == 1 :
  print("Odd numbers:", num2, num3)
elif num1 % 2 == 1 and num2 % 2 != 1 and num3 % 2 != 1 :
  print("Odd numbers:", num1)
elif num1 % 2 != 1 and num2 % 2 == 1 and num3 % 2 != 1 :
  print("Odd numbers:", num2)
elif num1 % 2 != 1 and num2 % 2 != 1 and num3 % 2 == 1 :
  print("Odd numbers:", num3)
else :
  print("No odd numbers here.")