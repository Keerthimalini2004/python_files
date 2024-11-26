'''a=3,4
print(a)'''

#tuple
'''t_=(45,3.4,'hai',(4,5),[2.5,3],45)
print(t_)
print(type(t_))'''
#single value tuple
'''t_1=(45,)          
print(t_1,type(t_1))'''
#constructor
'''print(tuple())
print(tuple('python'),
          tuple([4,5.3,True]),
          tuple({'a','b','c'}),
          tuple({3:45,False:45}))'''


#methods in tuple
#1.count
'''t_=(3,4,2.3,'apple',(4,),3.0,3)
print(t_.count(3))
print(t_.count('apple'))'''

#2.index
'''t_=(3,4,2.3,'apple',(4,),3.0)
print(t_.index(2.3))
print(t_.index(3))
print(t_.index(3,1))
print(t_.index('apple'))'''

#tuple is immutable error display
'''t_=(3,4,2.3,'apple',(4,),3.0)
t_[-1]=4.3
print(t_)'''

#operator in tuple
'''t_=(3,4,2.3,'apple',(4,),3.0)
t1=(45,3.4,'hai',(4,5),[2.5,3],45)
print(t_+t1)
print(t_*4)'''

#indexing
t1=(45,3.4,'hai',(4,5),[2.5,3],45)
print(t1[2])
print(t1[len(t1)-3])
print(t1[3][0])
print(t1[-2][1])

#slicing
t2=('23',[45,12,'895'],34.5,23,3+6j,False,0)
#to get even index element
print(len(t2))
print(t2[0:len(t2):2])
#to get odd index element
print(t2[1:len(t2):2])
#to reverse the list
print(t2[::-1])
#to get even index element in reverse
print(t2[-2::-2])
#to get odd index in reverse
print(t2[-1::-2])
#to reverse the list within list
print(t2[1][-1::-1])
#to reverse nested list[45,12,'895']
print(t2[1][::-1])












