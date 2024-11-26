                                       #COMPREHENSION
#usinf list
#1.program to square the numbers in a range
'''print([i*i for i in range(1,11)])'''

#2.program to square the numbers in a range only which is even
'''list_=[]
for i in range(1,11):
    if i%2==0:
        list_.append(i*i)
print(list_)'''

'''print([i*i for i in range(20,30) if i%2==0])'''

#3.program to print "even" if the numbers otherwise "odd"
num_=[32,54,44,66,34,87]
print(["even" if i%2==0 else "odd" for i in num_])

#4.program to convert string to uppercase
'''words=('hello','world','python')
for i in words:
     print(i.upper())'''

'''words=('hello','world','python')
print([i.upper() for i in words])'''

#5.program to fetch all the middle element in the list(not)
'''str_=input("enter:").split()
for word in str_:
       f_= len(word)//2
       print(word[f_])'''

'''str_=[1,2,3,4,5]
n=len(str_)
print([i if i%2==0 else [i//2] for i in n ])'''
#6.program to get middle characters of each word in a list
'''str_="hello world come here"
l_=[]
for s in l_:
       a=len(i)//2
       l.append(a[i])'''
       
'''lists=['jtdxg','yugtfv','yugjh','zsddxfc','uyjnuc']
l=[]
for word in lists:
    mid_ind=len(word)//2
    if len(word)%2!=0:
        l.append(word[mid_ind-1:mid_ind+1])
    else:
        l.append(word[mid_ind])
print(l)'''

'''lists=['jtdxg','yugtfv','yugjh','zsddxfc','uyjnuc']
print([len(word)//2 if len(word)%2!=0 else word[-1:+1] for word in lists])'''

#6.extract digits from a string(isnumeric)
'''text='a1b2c3'
print([i for i in text if i.isnumeric()])'''
    
#7.create a list of tuple with number and its cube
'''t=(2,3,4,5,5,6,7,8)
l=list(t)
print([(i,i**3) for i in l])'''
#8.filtering only the numbers divisible by 2 and 5
'''num=[55,43,78,75,40,9,68,7,90]
print([i for i in num if i%2==0 and i%5==0])'''
#9.extract 1st letter of each word if it is consonent(not a vowel)(not)
'''str_=input("enter the string:").split()
print([i for i in str_ if len(i) not in 'a,e,i,o,u' ])'''
#(doubt)
'''l1_=[]
for i in l_:
    if i[0] not in 'a,e,i,o,u':
        l1_.append(i)
print(l1_)'''
    
#10.program to fetch the fruits and its indexes if the indexes odd
'''fruits_=['apple','mango','kiwi','litchi','dragon fruit','orange']
print([(fruit,i) for i,fruit in enumerate(fruits_) if i%2!=0])'''

'''for i,fruit in enumerate(fruits_):
    if i%2!=0:
        print(i,fruit)'''
#11.program to fetch only repeated characters in a string(not)
'''str_=input("enter the string:")
count={}
for i in str_:
       if i in count:
           count+=1
       else:
            count=1
print(count)'''

'''input_="Hello world"  #set don't allow duplicate characters
print([char for char in set(input_) if input_.count(char)>1])'''
#12.create a list of dictionaries
'''keys=['name','age','city']
values=['malini',21,'Tamil nadu']
print([{keys[k]:values[k]} for k in range(len(keys))])'''

'''keys=['name','age','city']
values=['malini',21,'Tamil nadu']
d={}
for k in range (len(keys)):
    d[keys[k]]=values[k]
print(d)'''
    
#13.Customizing numbers
#create a comprehension  to print if the value is positive otherwise
#print negative if the number is negative
'''num_=(-5,0,10,-10)
print([v if v>=0 else "negative" for v in num_])'''
#14.reverse a string if the length of the string is more than 5
#otherwise print as it is
'''user_=input("enter the string:").split()
print([word[::-1] if len(word)>5 else word for word in user_])'''

'''user_=input("enter the string:").split()
for word in user_:
    if len(word)>5:
        print(word[::-1])
    else:
        print(word)'''



                   #--------DICTIONARY COMPREHENSION------#
#1.create a dictionary with word and its length
#1st try
'''dict_={'banana':3,'fries':45,'honey':6}
print({i:len(i) for i in dict_})'''

#normal
'''user_=input("enter the words:").split()
d={}
for word in user_:
    d[word]=len(word)
print(d)'''
#done by mam
'''user_=input("enter the words:").split( )
print({word:len(word) for word in user_})'''

#2.create a dictionary with chracter and its ascii value if the
#char is vowel
#for whole words
'''user_=input("enter the string:")
print({char:ord(char) for char in user_})'''
#crt
'''user_=input("enter the string:")
print({char:ord(char) for char in user_ if char in 'aeiouAEIOU'})'''

#3.create a dictionary with data and its length if the word length
#is less that 5 other wise reverse the word
'''user_=input("enter the string:").split()
print({word:len(word) if len(word)<5 else word[::-1] for word in user_})'''

'''user_=input("enter the string:").split()
d={}
for word in user_:
    if len(word)<5:
        d[word]=len(word)
    else:
        d[word]=word[::-1]
print(d)'''

#program to fetch the asscii value of last character of each word
'''str_=input("enter the string:").split()
for word in str_:
       a=(word[-1])
       print(ord(a))'''

'''str_=input("enter the string:").split()
print({char[-1]:ord(char[-1]) for char in str_ })'''

#wrong
'''str_=input("enter the string:")
d={}
for i in str_:
       d[str_[i]]=[i]
       print(d)'''

'''str_=input("enter the string:")
print({word:[i] for word in str_})'''

'''s={1,2,3,4,5}
l=set()
for i in s:
       a,b=i**2,i**3
       l.add((a,b))
print(l)'''





