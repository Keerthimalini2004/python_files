#map
'''def square_(set_):
    return set_ * set_
print(list(map(square_,set_)))
square_=lambda set_:set_*set_
print(list(map(square_,set_)))'''

#program to convert all the string in the list into uppercase
'''lis_=['Guys','Please','Concentrate','in','the','class']
li_=lambda l_:l_.upper()
print(list(map(li_,lis_)))
print(list(map(lambda k:k.upper(),lis_)))'''
#adding 2 lists element wise
'''list1=[1,2,3]
list2=[3,4,1]
print(list(map(lambda x,y:x+y,list1,list2)))'''

#multiply 2 lists element wise
'''list1=[1,2,3]
list2=[3,4,1]
t=[]
i=0
for i in range(len(list1)):
    t.append(list1[i]*list2[i])
print(t)'''

'''list1=[1,2,3]
list2=[3,4,1]
print(list(map(lambda x,y:x*y,list1,list2)))'''
#converting list of integers into string
'''li_=[6,78,57,34,8,4]
print(str(li_))
print(list(map(lambda l_:str(l_),li_)))'''

#mapping over a dictionary by incrementing each value by 1
'''data={'a':1,'b':2,'c':4}
print(tuple(map(lambda data_:{data_[0]:data_[1]+1},data.items())))'''
#extract name field from the dictionary
'''students=[{'name':'riya','age':20,'grade':'B'},
               {'name':'deepika','age':22,'grade':'A'},
               {'name':'keerthi','age':23,'grade':'C'},
               {'name':'jeeva','age':21,'grade':'A'}]
print(list(map(lambda n:n['name'],students)))'''

#program to find the square and cube pf set of numbers
'''list_=[2,7,56,8,4]
print(list(map(lambda li_:(li_**2,li_**3),list_)))'''

#square the numbers and get only even numbers
'''is_square=lambda n: n*n
is_even=lambda e_n:e_n%2==0
r_=range(1,10)
print(list(map(is_square,filter(is_square,r_))))'''

'''start_value=int(input("enter the number:"))
end_value=int(input("enter the number:"))
r_=range(start_value,end_value)
is_square=lambda n: n*n
is_even=lambda e_n:e_n%2==0
print(list(map(is_square,filter(is_even,r_))))'''

#get length of all the strings in a tuple
'''str_='apple','orange','mango','kiwi','grapes'
print(tuple(map(lambda k:len(k),str_)))'''
#rounding the numbers in set to 2  decimal point
'''floats_={1.234,2.3452,3.4234,5.3422,90.231}
print(set(map(lambda k:round(k,2),floats_)))'''
#program to reverse each list in a tuple
'''tuple_=[[3,2.4,2],[2.3,45,'12'],[34,12,2.3,True],[23,1]]
print(tuple(map(lambda k:k[::-1],tuple_)))
'''
                                                 #------qtalk-------(7/8/24)
#write a python

