#8.precision
'''
print(round(4.5623,1))
print(round(4.5423,1))
print(round(4.5623,2))
print(round(4.5423,2))
print(round(101.347231,4))
print(round(101.347231,3))
'''

#9.iskeyword
'''
"help('keyword')"
import keyword
print(keyword.iskeyword("True"))
print(keyword.iskeyword("Import"))
print(keyword.iskeyword("if"))
print(keyword.iskeyword("ELSE"))
'''
#10.isidentifier
'''print('num1'.isidentifier())
print('9a'.isidentifier())
print('a_1'.isidentifier())
print('_1a'.isidentifier())
print('a+'.isidentifier())'''

#11.divmod
'''n1=45
n2=5
print('division',n1/n2)
print('division',n1//n2)
print('remainder',n1%n2)
print(divmod(n1,n2))'''

#12.isinstance
'''print(isinstance(34,int))
print(isinstance('a',int))
print(isinstance(3.4,float))
print(isinstance(34-34j,(int,complex)))
print(isinstance(True,(int,complex)))
print(isinstance(6.7,(int,complex)))'''

#13.abs
'''print(abs(-87))
print(abs(8.5))'''

#14.trunc
'print(int(3.5))'
import math
print(math.trunc(65))
print(math.trunc(54.6))
print(math.trunc(43.6))


