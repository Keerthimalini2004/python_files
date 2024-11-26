                                               #-----------INHERITANCE------------
#i)single level inheritance
'''class Superclass_:
    class_name='superclass'

    def __int__(self):
        print("In superclass")

    def instance_me(self):
        print(self.class_name)

class subclass(Superclass_):
        def __init__(self):
            print("In Subclass")
            super().__init__()

obj1=subclass()
print(obj1.class_name)
obj1.instance_me()'''

#ii)multiple level inheritance
'''class Baseclass1:
    def __init__(self):
        self.a=10

class Baseclass2:
    def __init__(self):
        self.a=20

class subclass(Baseclass1,Baseclass2):
    def __init__(self):
        self.a=30
        print(self.a)
        super().__init__()

    def display_(self):
        print('Method in subclass')
        

c1=subclass()
print(c1.a)
c1.display_()'''

#iii)multilevel inheritance
'''class Baseclass:
    def __init__(self):
        self.a=10

    def display_(self):
        print('method is baseclass')

class subclass(Baseclass):
    def __init__(self):
        self.a=20
        print(self.a)
        super().__init__()

class subclass2(subclass):
    def display_(self):
        print(self.a)

ob1=subclass2()
print(ob1.a)'''

#iv)hierarchical inheritance
'''class Baseclass:
    def __init__(self):
        self.a=10
        print(self.a)

    def display_(self):
        print('method in baseclass')

class subclass(Baseclass):
    def __init__(self):
        print("in subclass")
        super().__init__()

class subclass2(Baseclass):
    def display_(self):
        print("method in subclass")
        super().display_()

obj1=subclass()
obj1.display_()
obj2=subclass2()
obj2.display_()'''


