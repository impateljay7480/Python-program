a =["jay","rumit","kaushal",["namn","jigar",["parth","krupal",["hello"]]]]
b = [1,2,3]
c = {2:"j",3:"a",4:"y"}

z = a+b

a.append("naman")

a.pop()

z = len(a)

a.pop(1)

a[0]="naman"

a.insert(2,"naman")

a[0]=["naman","jigar"]

print(a[3][2][2][0])

print(a[3][2][2][0][0::2])

a[1:3] = ["part"]

a[1:3] ="part"

b.extend(c)

b.extend(c.values())

b.extend(c.items())