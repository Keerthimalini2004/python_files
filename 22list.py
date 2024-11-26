#2.list
#homogeneous data type
'''list1=[34,5,7,24,87,446]
print(list1)
#heterogeneous-different datatypes
list2=['432',False,[54,65],23,865]
print(list2)
print("lenght :",len(list2))
print(type(list2))

#ii)constructor
#iii)default value
print(list())'''
#vi)default value []
#v)type casting
#string to list
    #1.according to characters  
'''print(list("bangalore is in karn"))
      #2.according to words
print("bangalore is in karn".split())

#tuple into list
print(list(('bangalore',34,4.5)))

#set into list
print(list({'bangalore',34,4.5}))

#dictionary into list
print(list({'bangalore':34,45:34,65:4.5}))'''

#slicing
'''list2=['23',[45,12,'895'],34.5,23,3+6j,False,0]
#to get even index element
print(len(list2))
print(list2[0:len(list2):2])
#to get odd index element
print(list2[1:len(list2):2])
#to reverse the list
print(list2[::-1])
#to get even index element in reverse
print(list2[-2::-2])
#to get odd index in reverse
print(list2[-1::-2])
#to reverse the list within list
print(list2[1][-1::-1])
#to reverse nested list[45,12,'895']
print(list2[1][::-1])'''

#reverse the string '23'
'''list2=['23',[45,12,'895'],34.5,23,3+6j,False,0]
print(list2[0][-1::-1])
#[34.5,23,6+6j]
print(list2[2:5:])'''

#list is immutable
'''str1='hello'
str1[1]='E'
print(str1)'''

#indexing
'''list2=['23',[45,12,'895'],34.5,23,3+6j,False,0]
list2[-2]='hey'
print(list2)
'''
#slicing
list2=['23',[45,12,'895'],34.5,23,3+6j,False,0]
list2[0:2]=[34,2]
print(list2)
list2[2:4]='apple'
print(list2)






