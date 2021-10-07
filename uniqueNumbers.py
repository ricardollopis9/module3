mylist = [10,2,3,4,4,4,3,3,3,56,7]
newlist = []

for i in mylist:
    if i not in newlist:
        newlist.append(i)

print(mylist)
print(newlist)
