list1 = list(range(-3,3))
print(list1)
list2 = list(range(-3, 6, 3))
print(list2)

grades = [58,85,95,78,80,94,99]
print(grades[1])
print(grades[0:2])
print(grades[-1])
print(min(grades))
print(max(grades))
print(sum(grades)/len(grades))
counter = 0
for grade in grades:
    if grade > 90:
        counter +=1
print("Number of A or A-‘s:", counter)
is_an_a = 100 in grades
print("Is there an A?", is_an_a)

languages = ["english","spanish", "chinese", "french"]
print("Popular in US:", languages)
languages.remove("french")
print(languages)
print("Remaining: ", len(languages))
languages.append("korean")
print(languages)
languages.insert(3,"tagalog")
print(languages)

languages.extend(["german", "arabic"])
print(languages)
colors = []
prompt ="Enter a color (or Enter to end): "
col = input(prompt)
while col != "        #the empty string
    colors.append(col)
    col = input(prompt)
    
print(colors)
if "black" in colors:
    colors.remove("black")
print(colors)
s = 'ab12c59p7dq'
digits = []

for symbol in s:
    if '1234567890'.find(symbol) != -1:
        digits.append(int(symbol))
print(digits)
digits.reverse()
print(digits)


subjects = ['bio', 'cs', 'math', 'history']

for item in subjects:
    print(item, end = "\t")
print(len(subjects))
print(min(subjects))
print(max(subjects))

subjects.sort()
print(subjects)

subjects.reverse()
print(subjects)
