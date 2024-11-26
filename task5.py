#9.7.24
#1)
'''s_="this is a bunch of words"
words_=s_.split()
w_=dict()
i=0
while i<len(words_):
    w_[words_[i]]=len(words_[i])
    i+=1
print(w_)'''

#2)
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

#3)
'''str_1='guido vann rossum'
d_=dict()
count=0
while count<len(str_1):
    d_[str_1[count]]=str_1.count(str_1[count])
    count+=1
print(d_)'''

#4)


#5)

#6)
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

#7)

#8)

#9)
'''l1=['hai','hello','12.3',10,34,3]
i=0
while i<len(l1):
    if type(l1[i])==int:
        print(l1[i])
    i+=1'''

#10)

#11)

#12)
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
ne_=''
while i<len(str_):
    if str_[i] in 'AEIOUaeiou':
        ne_=ne_+'*'
    else:
        ne_=ne_+str_[i]
    i+=1
print(ne_)









