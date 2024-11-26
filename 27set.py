#error
'''hash={'a',(4,),45,4.4,3-4j,False,'a'}
print('a',hash())
print(hash(4,5,6))
print(hash(4,5))'''

#type and len
'''set_={'a',(4,),45,4.4,3-4j,False,'a'}
print(set_)
print(type(set_))
print(set())
print(len(set_))'''

#typecasting
'''print(set("hello"))
print(set([3,4.5,(4,5),(4,)]))
print(set((3,4.5,(4,5),(4,))))
print(set({'a':1,'b':2,'c':3}))'''

#methods in set
#adding to or more sets
#1.add
'''set_1={'a',(4,),45,4.3,3-4j,False,'a'}
set_1.add("shivam")
set_1.add("jagan")
set_1.add((3,4))
print(set_1)'''

#2.union
'''set_1={'a',(4,),45,4.3,3-4j,False,'a'}
set_2={'a','b','c'}
set_3={4.5,3+4j,'kiwi',(9,8)}
print(set_1.union(set_2))
print(set_2.union(set_1,set_3))'''
#3.update
'''set_1={'a',(4,),45,4.3,3-4j,False,'a',55}
set_2={'a','b','c'}
set_3={4.5,3+4j,'kiwi',(9,8),55}
set_1.update(set_3)
print(set_1)
set_3.update(set_2,set_1)
print(set_3)'''
#removing a key from the set
#1.pop
'''set_1={'a',(4,),45,4.3,3-4j,False,'a'}
print(set_1.pop())
print(set_1.pop())
print(set_1)'''
#2.remove
'''set_1={'a',(4,),45,4.3,3-4j,False,'a'}
set_1.remove((4,))
print(set_1)
#keyerror
set_1.remove(23)
print(set_1)'''
#3.discard
'''set_1={'a',(4,),45,4.3,3-4j,67,'a'}
set_1.discard(67)
print(set_1)
set_1.discard(55)
print(set_1)'''

#date 28.6
#to get the common keys in set
#1.intersection
set_1={'a',(4,),45,4.3,3-4j,False,'a'}
set_2={'a','b','c'}
set_3={4.5,3+4j,'kiwi',(9,8)}
print(set_1.intersection(set_2))
print(set_2.intersection(set_1,set_3))
#intersection_update
set_1={'a',(4,),45,4.3,3-4j,False,'a'}
set_2={'a','b','c'}
set_3={4.5,3+4j,'kiwi',(9,8)}
set_2.intersection_update(set_1)
print(set_2)
set_1.intersection_update(set_2,set_3)
print(set_1)

#to get the uncommon keys in set
#1.difference
'''set_1={'a',(4,),45,4.3,3-4j,False,'a'}
set_2={'a','b','c'}
set_3={4.5,3+4j,'kiwi',(9,8)}
print(set_2.difference(set_1))
print(set_3.difference(set_1,set_2))'''
#2.difference_update
'''set_1={'a',(4,),45,4.3,3-4j,False,'a'}
set_2={'a','b','c'}
set_3={4.5,3+4j,'kiwi',(9,8)}
set_3.difference_update(set_1,set_2)
print(set_3)
set_2.difference_update(set_1)
print(set_2)'''
#3,symmetric_difference
set_1={'a',(4,),45,4.3,3-4j,False,'a'}
set_2={'a','b','c'}
set_3={4.5,3+4j,'kiwi',(9,8)}
print(set_2.symmetric_difference(set_1))
print(set_3.symmetric_difference(set_2))
print(set_1.symmetric_difference(set_3))
#4.symmetric_difference_update
set_1={'a',(4,),45,4.3,3-4j,False,'a'}
set_2={'a','b','c'}
set_3={4.5,3+4j,'kiwi',(9,8)}
set_3.symmetric_difference_update(set_1)
print(set_3)
set_1.symmetric_difference_update(set_2)
print(set_1)

#issubset
'''s1={3,'a','$%^',9.8}
s2={3,'a',3-4j,'$%^',9.8,(45,),56.4}
print(s1.issubset(s2))
s1={3,'a','$%^',9.8}
s2={3,'a',3-4j,'$%^',(45,),56.4}
print(s1.issubset(s2))'''

#issuperset
'''s1={3,'a','$%^',9.8}
s2={3,'a',3-4j,'$%^',(45,),56.4}
print(s1.issuperset(s2))'''

#isdisjoint
'''s3={3,4,5,7}
s4={34,56,12,4.5}
print(s3.isdisjoint(s4))'''

#oprators '-'--->difference(only take base set values)
'''s_={3,4,5.5}
s_1={4,'kiwi',55}
print(s_-s_1)
#i)^--->symmetric difference
s_={3,4,5.5}
s_1={4,'kiwi',55}
print(s_^s_1)
#ii)&---->intersection
s_={3,4,5.5}
s_1={4,'kiwi',55}
print(s_&s_1)

s_={3,4,5.5}
s_1={4,'kiwi',55}
print(s_&s_1&{4,5.6,55})
#iii)|--->union
s_={3,4,5.5}
s_1={4,'kiwi',55,3}
print(s_|s_1)'''



