# Find Armstrong Number

number =input("Enter Number:")

def armstrong_number(number):
    l = len(number)
    a = []
    for i in number:
        total = int(i) ** l
        a.append(total)
    s = sum(a)
    if int(number) == s:
        print(f"{number} is Armstrong Number")
    else:
        print(f"{number} is not Armstrong Number")

armstrong_number(number)