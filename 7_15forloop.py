'''str_='python'
for i in str_:
    print(i)'''

#eg for dictionary
'''dict_={'python':56,
       'java':56.5, 
       'perl':45,
       'css':True,
       45:'int',
       2.4:[4,5,6]}
#getkeys
for items in dict_:
    print(items)
for key in dict_.keys():
    print(key)
#get values
for v in dict_.values():
    print(v)
#get items
for item in dict_.items():
    print(item)
#unpack
for item in dict_.items():
    print(item[0],item[1])'''

#inbuilt function
#i)range
#1)program to print the numbers from 1 to 10
#*
'''i=1
while i<11:
    print(i)
    i+=1'''
#**
'''r1=range(1,11)
print(list(r1))
#***
for n in r1:
    print(n,end=' ')'''

#2)program to print the number from 10 to 1
'''for n in range (10,0,-1):
    print(n,end=' ')'''
#3)program to print the number from -10 to -1
'''for n in range(-10,0,1):
    print(n,end=' ')'''
#4)program to print the number from -10 to 5
'''for n in range(-10,6,1):
    print(n,end=' ')'''
#5)program to print the number from 20 to -15
'''for n in range(20,-16,-1):
    print(n,end=' ')'''
#6)program to print the number from -10 to 5
'''for n in range(-20,-14,1):
    print(n,end=' ')'''
#7)program to get only number from user input
'''n=int(input("enter the number:"))
n2=int(input("enter the number:"))
for i in range(n,n2,2):
    print(i)'''
                                         #2)enumerate
#program to get the word and index using for loop
'''s_=input("enter the string:").split()
t_=()
for index_ in range(len(s_)):
   t_+=((index_,s_[index_]),)
print(t_)'''

#program to get the word and index using enumerate
'''str_=input("enter the words:").split()
print(tuple(enumerate(str_)))
print(list(enumerate(str_)))
for t in enumerate(str_,1):
    print(t)'''

#create a tuple with index and length of the each word
'''str_="hello guys see on the screen and do this program"
t_=()
for i,word in enumerate(str_.split()):
    t_+=((i,len(word)),)
print(t_)'''

#create a set with index and word only with even length
'''str_="sharing is caring as always"
s_=set()
for i,word in enumerate(str_.split()):
    if len(word)%2==0:
        s_.add(word)
'print(str_.index(word[0],0,len(str_)),word[0])'
print(s_)'''

#create a dictionary with square  of index and 1st char of word.
'''str_=input("enter the words:")
dit_={}
for i,word in enumerate(str_.split()):
    dit_=({word[0]:(str_.index(word[0])**2)})
print(dit_)'''

                                                                      #3.zip
#zip
'''string_="exam"
lis_=[True,4,5.6,3+5j]
print(list(zip(string_,lis_)))'''
#zip_longest
'''string_="exam's"
lis_=[True,4,5.6,3+5j]
from itertools import zip_longest
for n in zip_longest(string_,lis_):
    print(n)
for n in zip_longest(string_,lis_,fillvalue='a'):
    print(n)'''

#program to add the numbers in the same indexes
'''n1=input("enter the elements:").split()
n2=input("enter the elements:").split()
from itertools import zip_longest
for i,j in zip_longest(n1,n2,fillvalue=10):
    print(int(i)+int(j))'''
    
#program to square the number in 1st and cube the number 2nd tuple
#and print in a tuple
'''n1=input("enter the elements:").split()
n2=input("enter the elements:").split()
from itertools import zip_longest
for i,j in zip_longest(tuple(n1),tuple(n2)):
    print((int(i)**2 ,int(j)**3 ))'''

#enumerate
#create a dict with index and fruit
'''fruits=['apple','mango','kiwi','cherry']
fruit_dict=dict(enumerate(fruits))
print(fruit_dict)'''

#take idex as power (eg: 4 power 0, 5 power 1....)
l_=[4,5,1,6]
l_1=[]
for i in enumerate(l_):
    l_1.append(i[1]**i[0])
print(l_1)




