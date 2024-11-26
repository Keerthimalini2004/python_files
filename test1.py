#1)
'''data=["hi","hello",10,"12.3",12,90,6.2]
i=0
while i<len(data):
    if (isinstance(data[i],int)):
        print(data[i])
    i+=1'''
#2)
'''data=["hi","hello",10,"12.3",12,90,6.2]
i=0
while i<len(data):
    if (isinstance(data[i],int)):
        print(data[i])
    elif (isinstance(data[i],float)):
        print(data[i])
    i+=1'''

'''data=["hi","hello",10,"12.3",12,90,6.2]
i=0
while i<len(data):
    if type(data[i])==int:
        print(data[i])
    elif type(data[i])==float:
       print(data[i])
    i+=1'''

#3.
'''str_=input("enter the filename:").split('.')
print(str_[-1])
'''
#4)
'''str_="hello welcome to python"
print(','.join(str_))'''

#5)
'''s="sony12india567pvt2ltd"
i=0
sum_=0
while i<len(s):
    if (s[i].isnumeric()):
        sum_+=int(s[i])
    i+=1
print(sum_)'''

#6)
'''str_="hELLo"
i=0
count=0
while i<len(str_):
    if (str_[i].isupper()):
        count=count+1
    i+=1
print(count)'''

#7)
'''s="@hello12world34welcome!123"
i=0
while i<len(s):
    if (not(s[i].isnumeric())):
        print(s[i])
    i+=1'''

#8)
'''names=['apple','google','apple','yahoo','google']
i=0
s=set()
while i<len(names):
    s+={names.intersection(
        '''

#9)
'''sen_='hello123world567welcometo9724python'
i=0
sum_=0
while i<len(sen_):
    if sen_.isnumeric():
        print(sen[i]%2==0)
    i+=1'''

#-10 to -1

'''i=-10
while i<=-1:
    print(i)
    i+=1
#-20 to 3
i=-20
while i<=3:
    print(i)
    i+=1
#1 to -5
i=1
while i>=-5:
    print(i)
    i-=1'''

#10)
                                                          #test1.(ii)

#1)
#2)
'''d={'a':'hello','b':100,'c':10.1,'d':'world'}
d_={}
for key,value in d.items():
    if isinstance(value,str):
        d_[key]=value[::-1]
    else:
        d_[key]=value
print(d_)'''

'''
d={'a':'hello','b':100,'c':10.1,'d':'world'}
d_={}
dict_items=d.items()
print(dict_items)
i=0
while i<len(dict_items):
    if (isinstance(dict_items[1],str)):
         d_[i][0]=[i][1][::-1]
    else:
        d_[i][o]=[i][1]
    i+=1
print(d_)'''

#3)
'''files=['apple.txt','yahoo.pdf','gmail.pdf','google.txt','amazon.pdf','facebook.txt','flipkart.pdf']
ext1='txt'
ext2='pdf'
file_ext={}
for file in files:
    f_e=file.split('.')
    if f_e[-1]==ext1:
        if ext1 not in file_ext:
            file_ext[ext1]=[f_e[0]]
        else:
            file_ext[ext1]+=[f_e[0]]
    elif f_e[-1]==ext2:
          if ext2 not in file_ext:
            file_ext[ext2]=[f_e[0]]
          else:
            file_ext[ext2]+=[f_e[0]]
print(file_ext)'''

#4)grouping flowers and animals in the below list
items_=['lotus-flower','lilly-flower','cat-animal','sunflower-flower','dog-animal']
d_={}
ext1='flower'
ext2='animal'
for file in items_:
    f_e=items_.split('-')
    if f_e[-1]==ext1:
        if f_e not in d_:
            d_[ext1]=[f_e[0]]
        else:
            d_[ext1]+=[f_e[0]]
    elif f_e[-1]==ext2:
        if f_e not in d_:
            d_[ext2]=[f_e[0]]
        else:
            d_[ext2]+=[f_e[0]]
print(d_)

#5)
'''names=['apple','google','apple','yahoo','yahoo','google','gmail','gmail','gmail']
i=0
d={}
while i<len(names):
    if names[0]==names[0]:
        d[names[i]]=[i]
    i+=1
print(d)'''
#done
'''names=['apple','google','apple','yahoo','yahoo','google','gmail','gmail','gmail']
d={}
for i,word in enumerate(names):
    if word not in d:
        d[word]=[i]
    else:
        d[word]+=[i]
print(d)'''














