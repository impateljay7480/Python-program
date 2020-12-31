
# Output : {'jay': {'maths': 1, 'eng': 2}, 'rumit': {'maths': 3, 'eng': 4}}

a = ['maths','eng']
f = []
key = ['jay','rumit']
for i in range(len(key)):
    b = []
    for i in range(len(a)):
        marks = int(input(f"enter marks of {a[i]}:"))
        b.append(marks)
    abc = dict(zip(a,b))
    f.append(abc)

d = dict(zip(key,f))
print(d)