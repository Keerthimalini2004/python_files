#1.program to check the given number is even or odd
'''num=int(input("enter the number:"))
if(num%2==0):
    print("the number is even")
else:
    print("the number is odd")'''

#2.write a program to check a character is vowel or not
#1.own
'''a=input("enter a character:")
vowels_='a','e','i','o','u'
if (a==a):
    print("a is a vowel")
elif(a==e):
    print("e is a vowel")
elif(a==i):
    print("e is a vowel")
elif(a==o):
    print("o is a vowel")
else:
    print("no match")'''
#2.
'''
a=input("enter a character:")
vowels_='a','e','i','o','u'
if a in vowels_: 
    print("vowels are matched")
else:
    print("no match")'''

#3.check whether the string is palindrome or not
'''a=str(input("enter the string:"))
if(a==a[::-1]):
    print("the given string is palindrome")
else:
    print("the given is not palindrome")'''

#4.check whether a number is palindrome or not
'''a=input("enter the number:")
if(a==a[::-1]):
    print("the given input is palindrome")
else:
    print("the given input is not palindrome")'''

#5.check whether a year is leap year or not
'''a=int(input("enter the year:"))
if(a%4==0):
    print("year is leapyear")
else:
    print("year is nonleap year")'''

#6.check whether the number is perfect square or not
'''i=int(input("enter the number:"))
s=i**0.5#produces the half value of the i input
if s*s==i:
    print("it is a perfect square")
else:
    print("it is not a perfect square")'''

#7.check if the given character is alphabet or number or special character
'''str_=input("enter the string:")
if(str_.isalpha()):
    print(" character")
elif(str_.isnumeric()):
    print("the character is number")
else:
    print("it is a special character")'''

#ii)doubt
'''str_=input("enter the string:")
if len(str_)==1 and char.isalpha():
    print("alphabets")
elif len(str_)==1 and str_.isnumeric():
    print("the character is number")
elif len(str_)==1 and not str_.isalnum():
    print("special character")
else:
    print("enter one character")'''

#8.pass mark or not
'''a=int(input("enter the number:"))
if(a>60):
    print("1st class")
elif 35<=a<60:
    print("pass")
else:
    print("fail")'''

#9.check the starting character of the string is vowel or not
'''s_=input("enter the string:")
start_str=s_[0]
if start_str in 'aeiouAEIOU':
    print("vowel")
else:
    print("not a vowel")'''

#10.check the given list has even length.
'''element=input("enter the element:").split()
if len(element)%2==0:
    print("even length")
else:
    print("odd length")'''

'''element=[1,2,3,4,5,6,7,8]
if len(element)%2==0:
    print("even length")
else:
    print("odd length")'''
#11.own0
'''dict_={'a':78,34:'int'}
if (len(dict_)%2==0):
    print("it is already even")
elif not len(dict_)%2==0:
    print("it is odd")
    dict_.update({45:2})
    print(dict_)
else:
    print("not possible")'''

#11.check the greatest number in user input        5.7.24
'''n1=int(input("enter:"))
n2=int(input("enter:"))
n3=int(input("enter:"))
if n1>=n2 and n1>=n3:
    print(n1,"is greatest")
elif n2>=n1 and n2>=n3:
    print(n2,"is greatest")
else:
    print(n3,"is greatest")'''

#12. in a number check if the first number is even or odd(done)
'''num_=input("enter the number:")
num2=str(num_[0])
if int(num2)%2==0:
    print(num2," is even")
else:
    print(num2,"is odd")'''

#13.in a number check if the second last number is even or odd
#done
'''num=input("enter the number:")
num1=str(num[-2])
if int(num1)%2==0:
    print(num1,"is even")
else:
    print(num1,"is odd")'''

#14.program to check if the given datatype is of string datatype
'''a_=int(input("enter:"))
if isinstance(a_,str):
    print("it is string datatype")
else:
    print("is is not string datatype")'''

#15.program to check a data is float datatype
'''a=float(input("enter the value:"))
if isinstance(a,float):
    print("the value is float")
else:
    print("the value is integer")'''

#16.program to check list is empty or not(done)
'''li=input("enter the value:")
if len(li)==0:
    print("empty")
else:
    print("not empty")'''

#17.program to return the length of string if character are present
#(done)
'''t=input("enter the string:")
a =t.isalnum()
if a:
    print("present")
    lenght=len(t)
    print("lenght is",lenght)
else:
    print("nothing")'''

#18.program to get the last element in the list(done)
'''li=input("enter the list:").split()
print(li[len(li)-1])'''

#19.program to get the middle character in the string(done)
'''s1=input("enter the string:")
mid=len(s1)//2
print(mid,s1[mid])'''

#20.program to check the data is number or special character
#done
'''a=input("enter the data:")
num=a.isnumeric()
if num:
    print("the entered data is number")
else:
    print("the entered data is not a number")'''

#21.program to check the integer is positive or negative(done)
'''num=int(input("enter the number:"))
if num>0:
    print("positive integer")
elif num<0:
    print("negative integer")
else:
    print("zero")'''

#22.program to smallest number in user input(done)
'''n1=int(input("enter the number:"))
n2=int(input("enter the number:"))
n3=int(input("enter the number:"))
if n1<n2 and n1<n3:
    print("n1 is smallest")
elif n2<n1 and n2<n3:
    print("n2 is smallest")
else:
    print("n3 is smallest")'''

#23.program to check the tuple is empty or not(done)
'''t=input("enter the data:")
if len(t)==0:
    print("the tuple is empty")
else:
    print("the tuple is not empty")'''

#24.program to check the number is divisible by 5 0r 8(done)
'''num=int(input("enter the number:"))
if num%5==0:
    print("the number is divisible by 5")
elif num%8==0:
    print("the number is divisible by 8")
else:
    print("invalid")'''

#25.constructor a marksheet using elif ladder(done)
'''mark=int(input("enter the number:"))
if mark>=90:
    print("grade a")
elif mark<90 and mark>=80:
    print("grade b")
elif mark<80 and mark>=60:
    print("grade c")
elif mark<60 and mark>=30:
    print("grade d")
else:
    print("fail")'''

#26.take the user input length and breadth of rectangle is equal print square or not
#done
'''length=int(input("enter the number:"))
breadth=int(input("enter the number:"))
if length==breadth:
    print("square")
else:
    print("not a square")'''

#27.program to check the number is prime or not
'''def prime_no(a):
    if a<=1:
        return False
    for i in range(2,a+1):
        if a%i==0:
            return False
        else:
            return True
     
print(prime_no(5))'''
