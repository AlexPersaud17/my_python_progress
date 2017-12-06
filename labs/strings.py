'''
word = "Python"

for letter in word:
    print(letter)

for letter in word:
    print(letter, sep = "-", end = "")

for ch in word:
    print(ch, end = "-")

word = "abracadabra"
count = 0
for ch in word:
    if ch == 'a':
        count += 1
print(count)

str1 = ("cha-" * 2) + "cha"
print(str1)

digits = '0123456789'
result = 100
for digit in digits:
    result -= int(digit)
    print(result)

digits = '0123456789'
result = ''
for digit in digits:
    result = result + digit * 2
    print(result)

for i in range(65, 75):
    print(chr(i), end="")

loud = "SCREAM"
result = ""
for letter in loud:
    result = result + chr(ord(letter) + 32)
    print(result)

word = input("Enter word: ")
reversed_w = ""
for ch in word:
    reversed_w = ch + reversed_w
print("The word reversed:", reversed_w)
'''
word = "Python"
print(len(word))
print(word[2])
print(word[2:])
print(word[-2])
print(word[-6:2])
print(word[3:])
