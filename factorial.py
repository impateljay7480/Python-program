# Python Program to Find the Factorial of a Number

n = int(input("Enter Number For Find Factorial:"))
t = 1
if 1 <= n:
    for i in range(1,n+1):
        t = t * i
    print(t)
else:
    print("Enter Valid Number")