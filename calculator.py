print("----------Welcome To Jp Calculator---------")

print("Enter the number:")
num1=int(input())
print("Enter the secound number:")
num2=int(input())
print("enter the operator:")
opt=input()
if opt == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif opt == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif opt == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif opt == "/":
    print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("Please Enter valid input....")
