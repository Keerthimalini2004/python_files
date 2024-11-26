#list methos
#1. i)append
'''l1=[56,"krithi",56.9,[7,9,5],[True,False]]
l1.append(5+4j)
l1.append("vasu")
print(l1)'''
#ii)extend
'''l2=[56,"krithi",56.9,[7,9,5],[True,False]]
l2.extend("vasu")
print(l2)
print(l2.extend)'''
#iii)insert
'''l3=[56,"krithi",56.9,[7,9,5],[True,False]]
l3.insert(3,789)
print(l3)'''


#2. i)pop
'''l3=[56,"krithi",56.9,[7,9,5],[True,False]]
l3.pop(3)
l3.pop()
print(l3)'''
#ii)remove
'''l3=[56,"krithi",56.9,67,3,8,56]
l3.remove(56)
l3.remove(56.9)
print(l3)'''
#iii)del
#indexing
'''l3=[56,"krithi",56.9,67,3,8,56]
del l3[2]
del l3[4]
print(l3)'''
#slicing
l3=[56,31,78,21,89,89,56]
'''del l3[2:5]
print(l3)'''

'''del l3[2:5]
print(l3)'''

'''del l3[::2]
print(l3)'''

'''del l3[1::2]
print(l3)'''


#3.reverse
'''l3=[56,"krithi",56.9,[7,9,5],[True,False]]
print(l3[::-1])
l3.reverse()
print(l3)
'''

#4.index
'''l3=['a',45,0,4.5,[7,9,5],True,False]
print(l3.index('a'))
print(l3.index(False,3)) #doubt
print(l3.index(True))'''

#5.count
'''l3=['a',45,'o',4.5,[4,3],True,1,False]
print(l3.count('a'))
print(l3.count(True)) #doubt
print(l3.count([4,3]))'''

#6.sort
'''list=['apple','Apple','grapes','van','TN','avacado']
list.sort()
print(list)
list.sort(reverse=False)
print(list)
list.sort(reverse=True)
print(list)'''

'''li=[True,False]
li.sort()
print(li)

l=['3+4j','2+3j','1+6j']
l.sort()
print(l)'''

#7.copying the list
 #1.normal copy
'''li_=['apple','Apple','grapes','van','TN','avacado']
li_1=li_
print(li_)
print(li_1)
print(id(li_),id(li_1))
print(id(li_[2]),id(li_1[2]))'''
#ii)swallow copy
#copy() 
'''li_=['apple','Appsxle',['grapes','van','TN'] ,'avacado'] 
li_1=li_.copy()
print(li_)
print(li_1)
print(id(li_),id(li_1))                    
print(id(li_[2]),id(li_1[2]))'''
#iii)deep copy
from copy import deepcopy
li_=['apple','Apple',['grapes','van','TN'] ,'avacado'] 
li_1=deepcopy(li_)
print(li_)
print(li_1)
print(id(li_),id(li_1))                    
print(id(li_[2]),id(li_1[2]))

#operators in list
'+'
'''list1=[43,32,'hospital','like']
list2=['apple','pepople',78,56,9]
print(list1+list2)
print(list2*2)'''

#function in previous topic
#15.ord and char
'''print(ord('t'),ord('1'),ord('&'))
print(chr(65),chr(100))
print(chr(2))'''















