                          #-------SORTED-------
#1.program to sort below list
'''numbers1=[3,1,4,6,5,74,67,3,9,6,3]
print(sorted(numbers1))
print(sorted(numbers1,reverse=True))'''

#2.program to sort according the length of string
'''random_words=['blank','makeup','one-day','dream','parlour','primer',]
print(sorted(random_words,key=len))'''

#3.sort according to the 1st character
'''random_words=['blank','makeup','one-day','dream','parlour','primer',]
print(sorted(random_words,key=lambda w:w[0]))
print(sorted(random_words))'''

#4.sort according to the last character.
'''random_words=['blank','makeup','one-day','dream','parlour','primer',]
print(sorted(random_words,key=lambda w:w[-1]))'''

#5.sorting values with absolute value
'''complex_numbers=[3+4j,1-1j,-1+2j,2+0j]
print(sorted(complex_numbers,key=abs))'''

#6.

#7.sorting a dictionary by keys
'''t_={'banana':3,'apple':5,'cherry':2,'dates':4}
print(dict(sorted(t_.items(),key=lambda t_:t_[0])))'''#for keys

#8.sorting a dictionary by values
'''t_={'banana':3,'apple':5,'cherry':2,'dates':4}
print(dict(sorted(t_.items(),key=lambda t_:t_[1])))'''#for values

#9.sorting a list of dictionary by a specific key
'''dict_list=[{'name':'kalai','age':63},{'name':'veena','age':22},{'name':'leela','age':45}]
print(sorted(dict_list,key=lambda dict_list:dict_list['age']))'''

#10.sorting with multiple keys
'''dict_list={'a':{'name':'kalai','age':63},'b':{'name':'veena','age':22},'c':{'name':'leela','age':45}}
print(dict(sorted(dict_list.items(),key=lambda item:(item[1]['age'],item[1]['name']))))'''

#11.sorting a list of list
'''data=[[1,2],[5,4],[2,3]]
print(sorted(data,key=lambda data:data[0]))'''

#12.sorting a length of tuples by length of strings
names={('bob','copper'),('charles','shetty'),('james','bond')}
print(sorted(names,key=lambda names:sum(len(y) for y in names)))


