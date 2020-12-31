a = {11:"jay",12:"rumit",13:"kaushal",22:"abhay"}
b = {"jay":"patel","rumit":"patel1","kaushal":"patel3"}
d = ["jay","rumit","kaushal"]
c =[1,2,3]

a[15]="parth"

a.update({16:"krupal"})

a[11]="kushal"

a.pop(11)

a.popitem()

a.setdefault(16,"lol")

b = a.copy()
print(b)

z = dict.fromkeys(d,c)

for i in range(len(d)):
    a[d[i]]=c

a.clear()

print(a)
