#1)program to print the number from 1 to 5
'''i=1
while i<=5:
    print(i)
    i=i+1 '''

#2)program to print the number from 5 to 1
'''i=5
while i>=1:
    print(i)
    i=i-1 '''

#3)write a program to print "bangalore" 10 times
'''i=1
while i<=10:
    print('bangalore',i)
    i=i+1'''

#4)write a program to print your name n times
'''n=int(input("enter the number:"))
count=1
while count<=n:
    print('malini',count)
    count=count+1'''
#done by mam
'''name=input("enter your name:")
n=int(input("enter the count:"))
i=1
while i<=n:
    print(name,i)
    i+=1'''
#5)write a program to print your name n times in reverse
'''name=input("enter your name:")
n=int(input("enter the count:"))
i=1
while i<=n:
    print(name[::-1],i)
    i+=1'''
#6)i)program to square the number from start to end
'''n1=int(input("starting value:"))
n2=int(input("ending value:"))
while n1<=n2:
    print(n1*n1)
    n1=n1+1'''

#ii)program to square the number from start to end
#with method---->append
'''n1=int(input("starting value:"))
n2=int(input("ending value:"))
l_=[]
while n1<=n2:
    l_.append(n1*n1)
    n1=n1+1
print(l_)'''

##iii)program to square the number from start to end
    #without method
'''n1=int(input("starting value:"))
n2=int(input("ending value:"))
l_=[]
while n1<=n2:
    l_=l_+[n1*n1]
    n1=n1+1
print(l_)'''

#7)i)program to get the character and its index
'''str_=input("enter the string:")
index_=0
while index_<len(str_):
      print(index_,str_[index_])
      index_+=1'''

#ii)program to get the character and its index using method
'''str_=input("enter the string:")
index_=0
l_=[]
while index_<len(str_):
      l_.append([index_,str_[index_]])#bracket note
      index_+=1
print(l_)'''
#using append method(pack as tuple in list)
'''str_=input("enter the string:")
index_=0
l_=()
while index_<len(str_):
      l_+=(index_,str_[index_])
      index_+=1
print(l_)'''

#8)i)program to print nested list with character and its ascii value
'''s1=input("enter the string:")
index_=0
while index_<len(s1):
    print(s1[index_],ord(s1[index_]))
    index_+=1
#nested list
s1=input("enter the string:")
index_=0
l1=[]
while index_<len(s1):
    l1.append([s1[index_],ord(s1[index_])])
    index_+=1
print(l1)'''
#ii)program to print nested list with character and its ascii value
#without method
'''s1=input("enter the string:")
index_=0
list_=[]
while index_<len(s1):
    list_+=[[s1[index_],ord(s1[index_])]]
    index_+=1
print(list_)'''

#9)program to get element and its length by taking input from user
a=input("enter the string:")
b=a.split()
index_=0
while index_<len(b):
      print(b[index_],len(b[index_]))
      index_+=1
      
    








    
    
