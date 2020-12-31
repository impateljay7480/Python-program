
print("Build a password generator and otp generator which takes length as user input")
import random
o = []
p = []


def OTP():
    otp = '0123456789'
    while True:
        n = int(input("otp length you wont it:"))
        for i in range(n):
            j = random.choice(otp)
            o.append(j)
        print(''.join(o))
        o.clear()

def PASSWORD():
    password = 'zxcvbnmasfdghjklpoiuytrewq0123456789@#$_%&'
    while True:
        n = int(input("password length you wont it:"))
        for i in range(n):
            j = random.choice(password)
            p.append(j)
        print(''.join(p))
        p.clear()

c = int(input("Enter 1 for otp & 2 for password:"))

if c == 1:
    OTP()
elif c == 2:
    PASSWORD()
else:
    print("Enter Valid input")
