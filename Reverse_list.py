
l = [1,2,3,4,5,6,7]
l1 = []
for i in range(len(l)):
    l1.insert(0,l[i])

l.clear()
l.extend(l1)
print(l)
# print(l1)
