word = "Gregory"
x = ""
word.lower()
for i in word:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        continue
    else:
        x = x + i
print(x)
