'''
s="banana"
print(s.index("na"))
print(s.index("an"))
print(s.count("na"))
print(s.count("a"))

praise = "Good dog".upper()
num_gees = praise.count("G")
print(num_gees)

num_gees = "Good dog".upper().count("G")
print(num_gees)

print("good dog".upper())
num_gees = "Good dog".count("G")
print(num_gees)

str1="Hello World"
print(str1.find("W"))
print(str1.find("l"))
print(str1.rfind("l"))
print(str1.find("x"))

s = "I think, therefore I am."
print(s.replace("I", "You"))
print(s.replace("I", "You", 1))
print(s.replace("I", "You", 5))
print(s.replace("He", "She", 5))
print(s)

str1 = 'one two three'
xlist = str1.split("-")
print(xlist)

str1 = 'one-two-three'
xlist = str1.split("-")
print(xlist)
'''
fullname = input("Full name: ")
n = fullname.rfind(" ")
print("Lastname:", fullname[n+1:])
print("Firstname:", fullname[:n])
