#1)i)packed way(append)
'''names=['apple','google','amazon','facebook','instagram','microsoft']
names.append(['netflix','prime','hotstar'])
print(names)'''

#ii)unpacked way so use (extend)
'''names=['apple','google','amazon','facebook','instagram','microsoft']
names.extend('netflix')
names.extend('prime')
print(names)'''

#2)difference between pop and remove
#i)pop
'''names=['apple','google','amazon','facebook','instagram','microsoft']
names.pop()
names.pop(3)
print(names)
#ii)remove
names=['apple','google','amazon','facebook','instagram','microsoft']
names.remove('instagram')
print(names)'''

#3)sort the list in descending order
'''names=['apple','google','amazon','facebook','instagram','microsoft']
names.sort(reverse=True)
print(names)'''

#4)eg to seperate by each characters and each word
'''string="developers in pyspiders"
print(list('developers in pyspiders'))
print('developers in pyspiders'.split())'''
