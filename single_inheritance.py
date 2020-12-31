

class parent:
    def __init__(self,a):
        self.name = "Jay"
        self.father_name = a

    def first(self):
        print(self.name)

class child(parent):

    def __init__(self,a):
        parent.__init__(self,a)
        self.surname = "Patel"

    def sec(self):
        print(self.surname,self.name,self.father_name)


obj= child("sureshbhai")
obj.sec()
