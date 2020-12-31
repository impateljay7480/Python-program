# Python Program to Check Prime Number

n = int(input("Enter Number To Check Prime or Not:"))

for i in range(2,n):
    if n % i == 0:
        print(f"{n} Not A Prime Number")
        break
else:
    print(f"{n} Is a Prime Number")
