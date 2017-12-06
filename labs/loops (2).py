'''
num = 3
while True:
	num = 2*num
	if num > 15:
		break
	print(num)

for i in range(1,5):
	print(i, i*i)

for d in [3, 1, 4, 5]:
	print(d)

for i in range(4):
	print("Hello")

for i in range(5):
	print(i, 2**i)

print("start")
for i in range(i):
	print("Hello")

for i in range(-1, -10, -2):
	print(i)

total = 0
for x in range(1,101,2):
	total += x
print(total)

for x in range(5):
	x += 5
	print(x)

x = 0
while x < 5:
	x += 5
	print(x)


for i in range(3):
	for j in range(4):
		print(i,"*", j, "=", i*j)

for i in range(7):
	for j in range(1, i + 2):
		print(j, end="")
	print()


for i in range(4):
	print("&" * (i + 1))


for i in range(4):
	for j in range(i + 1):
		print("&", end="")
	print()


for i in range(4):
	print("&" * (4 - i))


# Execute this by hand first
sum = 0
for i in range(5):
	for j in range(5):
		sum += 1
print(sum)


# Execute this by hand first
sum = 0
for i in range(5):
	for j in range(i+1, 5):
		sum += 1
print(sum)
'''

# Execute this by hand first
sum = 0
for i in range(5):
	sum += 1
for j in range(5):
	sum += 1
print(sum)




