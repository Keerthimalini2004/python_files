                                                  #------TYPES OF EXCEPTION HANDLING-------
#1.default exception handling
#using zerodivision error
'''n1=int(input("enter the number:")) #90
n2=int(input("enter the number:")) #0
try:
    print(n1/n2)
except Exception:
    print("number cannot be divisible by 0")'''

#using typeerror
'''n1=int(input("enter the number:")) 
try:
    print(n1+3)
except Exception:
    print("please check the type")'''

#2.specific exception handling
'''n1=int(input("enter the 1st number:")) 
n2=int(input("enter the 2nd number:"))
d={}
try:
    print(n1/n2)
    d[[4,5]]=90
    print(d)
except zerodivisionerror:
    print("divisible by 0")'''

#3.multiple exception handling
'''n1=int(input("enter the 1st number:")) 
n2=int(input("enter the 2nd number:"))
d={}
try:
    print(n1/n2)
    d[[4,5]]=90
    print(d)
except ZeroDivisionError:
    print("divisible by 0")
except TypeError:
    print("keys must be mutable")'''

#4.generic exception handling
'''n1=int(input("enter the 1st number:")) 
n2=int(input("enter the 2nd number:"))
d={}
try:
    print(n1/n2)
    d[{4,5}]=90
    print(d)
except ZeroDivisionError as Z:
    print(Z)
except TypeError as T:
    print(T) '''
#RAISE
'''print('----INSTAGRAM----')
password_=input("enter your password:")
PW='Jsp@123'
try:
    if password_t==PW:
        print("Login Successfully")
    else:
        raise exception
except Exception:
    print('invalid password')'''
