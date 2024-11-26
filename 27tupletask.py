#1)how to create single value tuple
'''t1=(45,)
print(t1)'''

#2)relation between id1 and id2
'''t1=(1,2,3)
id1=id(t1)
print(id1)
t2=(4,5,6)
id2=id(t2)
print(id2)'''

#3)doubt
'''t1=(1,2,3)
t2=(4,5,6)
print(*t1,*t2)'''

#4)i)replace y to Y
t=(1,2,3,4,['hai','hello',123],'python')
t3=list(t)
t3.replace(
s=tuple(t3)
print(s)
#ii)replace 1,2,3 into 9,10,11
'''t=(1,2,3,4,['hai','hello',123],'python')
t2=list(t)
t2[0]=9
t2[1]=10
t2[2]=11
x=tuple(t2)
print(x)'''

#5)i)add elements in tuple
'''t5=(5,7,59,89.5)
t=list(t5)
t.append(34)
y=tuple(t)
print(y)'''


#6)remove two elements from the tuple
'''t=(1,2,3,4,['hai','hello',123],'python')
j=list(t)
j.remove(3)
j.remove('python') 
print(tuple(j))'''
