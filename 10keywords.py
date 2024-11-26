#to display all keywords
'''
help('keywords')
help("keywords")
'''

#to display keywords using import
'''
import keyword
keyword.kwlist
print(keyword.kwlist)
'''

#keyword is not modifiable
'''
print(True)
print(true)
'''

#1.identifiers
'''
a1=10
print(a1)
'''
#2.
'''
_a,a_1,a_=3,12,4.4
print(_a,a_1,a_)
'''
#3.error
'''
$j='hi'
print($j)
'''

#variables
'''
myname="pyspiders"
print(myname)
bool_=False
print(bool_)
'''
#case 1
'''
n1,n2=24,45
print(n1,n2)
'''
#case 2
#variable is same and value is different
'''
c1='a'  #a is stored in garbage collector
c1='b'
print(c1)
'''

#case 3
#variable is different and value is same
'''
c1='a'
c2='a'
print(c1,c2)
print(id(c1))
print(id(c2))
print(id('a'))
'''
#keyword cannot be a variable
'''
Import=76
print(Import)#if we use small import it doesn't work
'''

#3.constant
'''
pi = 3.14  #for variable so lowercase
print(pi)

PI = 3.14
print(PI)
'''

#inbuild function
#1.






