print("banana".index("na"))
print("banana".index("an"))
print("banana".count("na"))
print("banana".count("a"))

praise = "Good dog".upper()
num_gees = praise.count("G")
print(num_gees)

num_gees="Good dog".upper().count("G")
print(num_gees)
print("Good dog".upper())
num_gees = "Good dog".count("G")
print(num_gees)

str1 = "Hello World"
print(str1.find("W"))
print(str1.find("l")
print(str1.rfind("l"))
print(str1.find("x"))

s = "I think, therefore I am."
print(s.replace("I", "You"))
print(s.replace("I", "You", 1))
print(s)
s = "I I I I I."
print(s.replace("I", "You", 4))
print(s)
print(s.replace("You", "I")
print(s)

str1 = "one two three"
xlist = str1.split()
print(xlist)

str1 = "one-two-three"
xlist = str1.split("-")
print(xlist)

fullname = input("Full Name:")
n = fullname.rfind(" ")
print("Lastname:", fullname[n+1:])

s = "   Hello, World   "
els = s.count("l")
print(els)
print("***" + s.strip() + "***")
print("***" + s.lstrip() + "***")
print("***" + s.rstrip() + "***")
news = s.replace("o", "***")
print(news)

person = input("Enter your name: ")
greeting = ‘Hello {}’.format(person)
print(greeting)

orig_price = 75
discount = 15
new_price = (1-discount/100)*orig_price
calc = "${:.2f} discounted by {} % is ${:.2f}".format(orig_price,discount,new_price)
print(calc)

x = 2
y = 6
print("sum of {0} and {1}: {3}, product:{2}".format(x,y,x*y,!x+y))

for i in range(65, 75):
    print(chr(i), end="")

loud = "SCREAM"
result = ""
for letter in loud:
    result = result + chr(ord(letter) + 32)
    print(result)


word = input("Enter word:")
reversed = ""
for ch in word:
    reversed = ch + reversed
print("The word reversed:", reversed)
