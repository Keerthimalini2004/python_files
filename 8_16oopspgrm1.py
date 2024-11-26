#1.calcation for to find percentage,average and total
'''class calculation:
    def __init__(self,stu_name,reg_no,stu_marks):
        self.student_name=stu_name
        self.register_no=reg_no
        self.marks=stu_marks

    def student_details(self):
        return f'''
       # name:{self.student_name}
        #reg_no:{self.register_no}'''
'''   def total_marks(self):
        return sum(self.marks)

    def average_mark(self):
        return self.total_marks()/len(self.marks)

    def percentage(self):
        return (self.marks()/300)*100

student1=calculation('malini',67,[67,98,54])
print(student1.student_details())
print("the total mark is ",student1.total_marks())
print("Average:",student1.average_mark())
print("percentage:",student1.percentage())'''

#2.ATM
'''class ATM:
    def __init__(self,name,amount,language):
        self.name=name
        self.amount=amount
        self.language=language

    def deposite_amt(self,amount_dep):
        self.amount+=amount_dep
        return self.amount
    def withdraw_amt(self,withdraw_amt):
        self.amount -= withdraw_amt
        return self.amount
    def display(self):
        return self.amount
atm1=ATM('malini',45677,'tamil')
print(atm1.deposite_amt(1000))
print(atm1.withdraw_amt(500))
print(atm1.display())'''

#3)rectangle
'''class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def d1(self):
        return f'''
#        length:{self.length}
#        width:{self.width}'''
'''    def area(self):
        return self.length*self.width

    def perimeter(self):
        return (self.length+self.width)*2

data1=Rectangle(2,4)
print(data1.d1())
print(data1.area())
print(data1.perimeter())'''

#4.string
'''class String:
    def __init__(self,string):
        
        self.string=string

    def reversed(self):
'''        '''n=input("enter the string")
        i=0
        st_=' '
        while i<len(n):
            st_=n[i]+st_
            i+=1
        return st_'''  '''
        return self.string[::-1]

    def add(self):
        a=input("enter the string1:")
        b=input("enter the string2:")
        return a+b

    def st_(self):
'''        '''a=input("enter the string:")
        return '-'.join(a)'''   '''
        return '-'.join(self.string)

    def mid_(self):
        b_=len(self.string)//2
        return b_

    
d1=String('dfgh')
print(d1.reversed())
print(d1.add())
print(d1.st_())
print(d1.mid_())'''

#5.o/p:apbqcr
'''class Word:
    def __init__(self,w1,w2):
        self.word2=w1
        self.word1=w2
        
    def display(self):
        new_str=' '
        for a,b in zip(self.word2,self.word1):
            new_str+=a
            new_str+=b
        return new_str

data1=Word('abc','pqr')
print(data1.display())'''

#6
'''class A:
    def __init__(self,word1):
        self.word1=word1

    def display(self):
        return str(self.word1)=='abab'
word=A('abab')
print(word.display())
word=A('ababc')
print(word.display())'''
#in class   (without class)
'''a_=input("enter the string:")
double_str=a_*2
m_string=double_str[1:-1]
if a_ in double_str:
    print(a_.count(a_[:2]))
else:
    print(False)'''


#removing duplicates
'''class A:
    def __init__(self,string_):
        self.str_=' '

    def repeated_(self):
        self.m_s=(self.a_+self.a_)[1:-1]
        if self.a_ in self.m_s:
            for char in self.a:
                if char not in self.str_:
                    self.str_+=char
                print(f{self.str_},is repeated,{self.a_.count(self.a_
'''
    
'''a_=input("enter:")
d_str_=(a_+a_)[1:-1]
str_=' '
if a_ in d_str_:
    for char in a_:
        if char not in str_:
            str_+=char
    print(a_.count(a_[:len(str_)]))
else:
    print(False)'''
#7.
'''class Object1():
    def __init__(self,value):
        self.val=value

    def zero(self):
        return sorted(self.val,key=lambda x:x==0)

c1=Object1([0,1,0,3,12])
print(c1.zero())
c2=Object1([0])
print(c2.zero())'''

#8.
'''class C():
    def __init__(self,n):
        self.value=n

    def value(self):
        if self.value<10:
            return [1,(self.n+1)%10]
        else:
            return [(int(d)+1)%10  for d in str(self.n)]

b1=C(1234)
print(b1.value())
a1=C(9)
print(a1.value())
'''
#xyxxyx
'''a_='xyxxyx'
str_=' '
'''
#without class
'''def find_repeated_substring(s):
    n = len(s)
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            substring = s[:i]
            repeated_times = n // i

            if substring * repeated_times == s:
                return f'{substring}:{repeated_times}'

    return False


input1 = 'xyxxyxxyx'
output1 = find_repeated_substring(input1)
print(f'input: {input1}\n output: {output1}')'''

#3.9.24
#name and age in single inheritance
'''class A:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"name:{self.name},age:{self.age}")
class B:
    def __init__(self,state):
        self.state=state
    def vote(self,age):
        if age>=18:
            print(f"{self.state}.{age} is eligible to vote")
        else:
            print(f"{self.state}.{age} is not eligible to vote")
person=A("keerthi",21)
person.display()
vote=B("ap")
vote.vote(person.age)'''

#hierarchical inheritance
class Baseclass:
    def __init__(self):
        self.a=10
    def display_(self):
        print("method in Baseclass")

class Subclass1(Baseclass):
    def __init__(self):
        self.a=20
        print("in subclass")
        super().__init__()
class Subclass2(Baseclass):
    def dispaly_(self):
        print("method in subclass2")
        super.display_()
obj1=Subclass1()
obj1.display_()
obj2=Subclass2()
obj2.display_()
        
#multilevel inheritance
'''class Baseclass:
    def __init__(self):
        self.a=10
    def display_(self):
        print("method in Baseclass")

class Subclass1(Baseclass):
    def __init__(self):
        self.a=20
        print(self.a)
        super().__init__()
class Subclass2(Baseclass):
    def dispaly_(self):
        print(self.a)
obj1=Subclass2()
print(obj1.a)
obj2=Subclass1()
print(obj2.a)
'''
    
        
