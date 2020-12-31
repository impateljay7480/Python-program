class a:
    def __init__(self):
        self.add = "patan"
        self.dob = 111


    def first(self,a):
        self.name = a
        print(self.name)

class b:

    def __init__(self):
        self.dob = 222
        print(self.dob)

    def sec(self,b):
        self.surname = b
        print(self.surname,self.dob)

class c(a,b):

    def __init__(self):
        super().__init__()
        self.dob = 333
        # print(self.dob)

    def third(self,age):
        self.age = age
        super().sec(b="patel")
        print(self.age)

# o = a()
# o.first("jay")
#
# new_o = b()
# new_o.sec("patel")

# new_sec_o = c()
# new_sec_o.third(23)
# new_sec_o.sec('patel')
# new_sec_o.first("jay")


check_super = c()
check_super.third(22)
# check_super.third(55)