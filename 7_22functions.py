#functions
'''list_=[5,6,7,8]
tuple_=(4,5,6,7)
print(len(list_),len(tuple_))'''

#reusability
#1)program to get length of any iterable without method
'''def length_(iterable):
    print(len(iterable))


length_([5,6,7,8])
length_((4,5,6,8,7))'''

#2)program to get length of any iterable without method
'''def length_(str_):
    count=0
    for i in str_:
        count+=1
        print(count)
length_([5,6,7,8])
length_((5,2,5,6,9,4))'''

                                 #variable scope
#1)global scope
'''a=10
def f1():
    print(a,"inside the function")

f1()
print(a,"outside the function")'''

#2)local scope
'''a=10
def f1():
    a=20
    print(a,"inside the function")

f1()
print(a,"outside the function")
#2)i)convert local to global 
a=10
def f1():
    global a
    a=20
    print(a,"inside the function")

f1()
print(a,"outside the function")'''
#2)ii)return keyword
'''a=10
def f1():
    a=10
    return a
a1=f1()
print(a1)'''

'''def f1():
    return
a1=f1()
print(a1)'''

'''def f1(a,b):
     return a+b
a1=f1(10,20)
print(a1)

def f1(a,b):
     return a+b,a*b
a1=f1(10,20)
print(a1)'''

#3)non local variable
'''def f1():
    num=100
    def f2():
        num=200 #non local variable
        print(num)
    f2()
    print(num)
f1()

#convert the non local variable to global
def f1():
    num=100
    def f2():
        nonlocal num
        num=200 
        print(num)
    f2()
    print(num)
f1()'''

'''def func(str_,n):
    if n==0:
        print(str_[1::2])
    elif n==1:
        print(str_[::2])'''

#3)recursive function
#to know recursion limit
'''import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(20)
print(sys.getrecursionlimit())'''
#exception
'''def func_name():
     print('hai')
     func_name()
func_name()'''

#eg
'''def print_(i=1,l_=[]):
    if i<=10:
        l_.append(i)
        return print_(i+1,l_)
    else:
        return l_
print(print_())'''

                                                                        #qtalk
#1)write a functions to check if the number is prime
'''number=int(input("enter the number:")) 
def fun_number():
    for n in range(2,number):
        if number%n==0:
            print("it is not a prime number")
            break
    else:
            print("it is a prime number")
fun_number()'''

#2)write a method that returns last digit of an integer.
'''num=input("enter the number:")
def get_last_digit():
        print(num[-1])
get_last_digit()'''

#3)make a function named tail that takes a sequence(like a list,string,or tuple)and a number n
#and returns the last n elements from the guven sequence,as a list

#4)

#practice problems(recursion)
#1)program to print numbers from 20 to 10
'''def fun_1(i=20,l_=[]):
    if i>=10:
       l_.append(i)
       return fun_1(i-1,l_)
    else:
        return l_
print(fun_1())'''

#2)program to get numbers from 1 to 5 and sum it
'''def sum_numbers(i=1,sum_=0):
    if i<=5:
        return sum_numbers(i+1,sum_+i)
    else:
        return sum_
print(sum_numbers())'''

#3)program to get factorial of a number
'''num=int(input("enter the number:")) 
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1) 
print(factorial(num)) '''

'''def print_(i=1,fact_=1):
    if i<=5:
        fact_=fact_*i
        return print_(i+1,fact_)
    else:
        return fact_
print(print_())'''
#4)program to get sum of digits(not done)
'''def sum_numbers(n_,i=1,sum_=0):
    if i<=n_:
        return sum_numbers(n_,i+1,sum_+i)
    else:
        return sum_
print(sum_numbers(n_))'''
#5)program to reverse a string
'''def re_st(i=0,ne_s=' ',str_=input("enter the string:")):
    if i<len(str_):                                                                #i=0 
            ne_s=str_[i]+ne_s
            return re_st(i+1,ne_s,str_)
    else:
            return ne_s
print(re_st())'''
#6)greatest common divisor
'''def gcd(a,b):
        if b==0:
                return a
        else:
                return gcd(b,a%b)
print(gcd(25,5))'''
#7)program to convert uppercase each word in a tuple
#8)fibbonacci sequence
09def print_(a=0,b=1,
