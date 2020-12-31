import re

pattern = '^[a-z0-9]+[.]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
email = 'pateljay1612@gmail.com'

if re.match(pattern,email):
    print("match")
else:
    print("not match")

# y=re.match(pattern,email)
# print(y)
# x = re.search(pattern,email)
# print(x)