class parent:
    def __init__(self):
        self.name = "Jay"

    def first(self):
        print(self.name)

class child(parent):

    def __init__(self):
        parent.__init__(self)
        self.surname = "Patel"

    def sec(self):
        print(self.name,self.surname)

class sub_child(child):

    def __init__(self,e):
        child.__init__(self)
        self.age = e

    def third(self):
        print(self.name,self.surname,self.age)



sub_new_o = sub_child(22)
sub_new_o.third()