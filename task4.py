#6.7.24(qtalk)
#1)program to convert lowercase to upper
'''str_=input("enter the string:")
print(str_.upper())'''

'''str_=input("enter the string:")
i=0
while i<len(str_):
    print(str_.upper())
    break'''

'''str_=input("enter the string:")
i=0
st=' '
while i<len(str_):
    if 'a'<=str_<='z':
        st+=(chr(ord(str_)-32))
    else:
        st+=str_[i]
    i+=1
print(st)'''

#without else part(best one)
'''str_=input("enter the string:")
i=0
while i<len(str_):
    if 'a'<=str_<='z':
        print(chr(ord(str_)-32))
    i+=1'''

#2)program to convert upper to lowercase
'''str_=input("enter the string:")
print(str_.lower())'''

'''str_=input("enter the string:")
i=0
st=' '
while i<len(str_):
    if 'A'<=str_<='Z':
        st+=chr(ord(str_)+32)
    else:
        st+=str_[i]
    i+=1
print(st)'''
#without else part
'''str_=input("enter the string:")
i=0
while i<len(str_):
    if 'A'<=str_<='Z':
        print(chr(ord(str_)+32))
    i+=1'''
#3)program to convert upper to lowercase and lowercase to upper
#using method
'''str_=input("enter the string:")
i=0
s=' '
while i<len(str_):
    if (str_[i]==str_[i].upper()):
        print(str_[i].lower())
    else:
        print(str_[i].upper())
    i+=1
print(s)'''

#4)program to convert upper to lowercase and lowercase to upper without using method
'''str_=input("enter the string:")
if ('a'<=str_<='z'):
    print(chr(ord(str_)-32))
elif ('A'<=str_<='Z'):
    print(chr(ord(str_)+32))
else:
    print("invalid")'''
    
#5)print the index and character of a string
'''str_=input("enter the string:")
index_=0
while index_<len(str_):
    print([index_,str_[index_]])
    index_+=1'''
#6)program to convert upper to lowercase and lowercase to upper without using method
#for more than one character
'''str_=input("enter the string:")
index_=0
new_str=' '
while index_<len(str_):
    if 'a'<=str_[index_]<='z':
        new_str+=(chr(ord(str_[index_])-32))
    elif ('A'<=str_[index_]<='Z'):
        new_str+=(chr(ord(str_[index_])+32))
    else:
        new_str+=str_[index_]
    index_+=1
print(new_str)'''

#7)program to get the string in reverse order
'''str_=input("enter the string:")
print(str_[::-1])'''

'''str_=input("enter the string:")
i=0
while i<len(str_):
     i+=1
print(str_[::-1])'''
  
#8)program to get the length of string in a list
'''names=['eve','james','bill','steve','mill','amul']
print(len(names))'''

'''names=['eve','james','bill','steve','mill','amul']
i=0
while i<len(names):
    print(names[i],len(names[i]))
    i+=1'''

#9)program to get the 1st character of each string in the list
'''names=['eve','james','bill','steve','mill','amul']
l_=[]
index_=0
while index_<len(names):
    l_.append(names[index_][0])
    index_+=1
print(l_)'''
#10)program to get the last character of each string in the list
'''names=['eve','james','bill','steve','mill','amul']
l_=[]
index_=0
while index_<len(names):
    l_.append(names[index_][-1])
    index_+=1
print(l_)'''
#11)create a dictionary with starting character and word in the list
'''names=['eve','james','bill','steve','mill','amul']
d_={}

index_=0
while index_<len(names):
    d_[names[index_][0]]=names[index_]
    index_+=1
print(d_)'''
#12)create a dictionary with word and length word in the list
'''names=['eve','james','bill','steve','mill','amul']
dict_={}
index_=0
while index_<len(names):
    dict_[names[index_]]=len(names[index_])
    index_+=1
print(dict_)'''

#13)program to print only the words starting with vowel
'''names=['eve','james','bill','steve','mill','amul']
i=0
st_=' '
while i<len(names):
    if (names[i][0] in ('a','e','i','o','u')):
        st_+=names[i]
    i+=1
print(st_)'''
#14)program to get the numbers which is of even
'''l_=[2,3,4,45,43,89,12,90,77,65]
i=0
while i<len(l_):
      if(l_[i]%2==0):
          print(l_[i])
      i+=1  '''
#15)program to get the numbers which is of odd
'''l_=[2,3,4,45,43,89,12,90,77,65]
i=0
while i<len(l_):
      if(l_[i]%2!=0):
          print(l_[i])
      i+=1  '''

#16)program to get the numbers starting with even numbers
'''l=[2,3,4,45,43,89,12,90,77,65,34,234,89,45,620]
i=0
while i<len(l):
    if(l[i][0]%2==0):
       print(l) 
    i+=1'''

#17)program to get the numbers starting with odd numbers
'''l=[2,3,4,45,43,89,12,90,77,65,34,234,89,45,620]
i=0
while i<len(l):
    if(l[i][0]%2!=0):
       print(l) 
    i+=1'''

#18)program to get 1 to 10
#i)
'''i=1
while i<=10:
    print(i)
    i+=1'''
#ii)program to get -1 to -10
'''i=-1
while i>=-10:
    print(i)
    i-=1'''
#iii)program to get 10 to 1
'''i=10
while i>=1:
    print(i)
    i-=1'''
#iv)program to get 1 to user input
'''a=int(input("enter the number:"))
i=1
while i<=a:
    print(i)
    i+=1'''
#v)program to get -20 to -10
'''i=-20
while i<=-10:
    print(i)
    i+=1'''
#vi)program to get 1 to -10
'''i=1
while i>=-10:
    print(i)
    i-=1'''
#vii)program to get -1 to 20
'''i=-1
while i<=20:
    print(i)
    i+=1'''
#viii)program to get -10 to -1(important)
'''i=-10
while i<=-1:
    print(i)
    i+=1'''

#9.7.24
#1)building a dictionary of a word and length pair of word -"this is a bunch of words
#mam
'''s_="this is a bunch of words"
words_=s_.split()
w_=dict()
i=0
while i<len(words_):
    w_[words_[i]]=len(words_[i])
    i+=1
print(w_)'''
#own
'''s_="this is a bunch of words"
l=s_.split()
d={}
i=0
while i<len(l):
    d[l[i]]=len(l[i])
    i+=1
print(d)'''
#2)fliping keys and values of the dictionary
#mam
'''dict_={'a':1,'b':4,'c':8}
items_=dict_.items()
items_list=list(items_)
print(items_list)
d_={}
i=0
while i<len(list(items_)):
    d_[items_list[i][1]]=items_list[i][0]
    i+=1
print(d_)'''
#own
'''dict_={'a':1,'b':4,'c':8}
a=dict_.items()
b=list(a)
print(b)
i=0
d={}
while i<len(dict_):
    d[b[i][1]]=b[i][0]
    i+=1
print(d)'''

#3)program to count the number of each characters in a string
'''str_1='guido vann rossum'
d_=dict()
count=0
while count<len(str_1):
    d_[str_1[count]]=str_1.count(str_1[count])
    count+=1
print(d_)'''
#own
'''str_1='guido vann rossum'
d_={}
i=0
count=0
while i<len(str_1):
    d_[str_1[i]]=str_1.count(str_1[i])
    i+=1
print(d_)'''

#4)program to create a dictionary with word and its count(own)
'''str_='hello world welcome to python hello hi world welcome to java'
a=str_.split()
count=0
i=0
d_={}
while i<len(a):
    d_[a[i]]=a.count(a[i])
    i+=1
print(d_)'''

#5)dictionary of character and ASCII value pair:
'''s="absABS"
i=0
d={}
while i<len(s):
    d[s[i]]=ord(s[i])
    i+=1
print(d)'''
#6)building a dictionary whose price value is more than 200
'''price_={"AMEC":24.45,"APAL":612.45,"IBM":200.45,"HP":37.80,
                     "FB":10.75}
price_tuple=tuple(price_.items())
d_={}
i=0
while i<len(price_tuple):
    if price_tuple[i][1]>200:
        d_[price_tuple[i][0]]=price_tuple[i][1]
    i+=1
print(d_)'''

#7)program to get all the alphabets from the string
'''str_=input("enter the string:")
i=0
s=' '
while i<len(str_):
    if (str_[i].isalpha()):
        s+=str_[i]
    i+=1
print(s)'''

#8)program to get all the special characters from the string
'''str_=input("enter the string:")
i=0
while i<len(str_):
    if (not(str_[i].isalnum())):
        print(str_[i])
    i+=1'''

#9)program to get only integer from the list
l1=['hai','hello','12.3',10,34,3]
i=0
while i<len(l1):
    if isinstance(l1[i],int):
        print(l1[i])
    i+=1

#10)progarm to print only vowels in a string
'''s="python selenium"
i=0
s_=' '
while i<len(s):
    if (s[i] in ('a','e','i','o','u')):
        s_+=s[i]
    i+=1
print(s_)'''

#11)program to get only alphanumeric characters from the string
'''s=input("enter the string:")
i=0
s_=' '
while i<len(s):
    if (s[i].isalnum()):
        s_+=s[i]
    i+=1
print(s_)'''

#12)write a program to check if the given list of string which is palindrome
'''elements_=input("enter some elements:\n").split()
i=0
l_=[]
while i<len(elements_):
    if elements_[i]==elements_[i][::-1]:
        l_+=[elements_[i]]
    i+=1
print(l_)'''

#13)
str_="hello world"
i=0
ne_=' ' 
a='AEIOUaeiou'
while i<len(str_):
    if str_[i] in a:
        ne_=ne_+'*'
    else:
        ne_=ne_+str_[i]
    i+=1
print(ne_)











