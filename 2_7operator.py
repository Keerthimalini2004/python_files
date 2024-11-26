#1.arithmetic operator
'''+,-,*,/,//,%,**'''
#2.relational operator
'<,>,<=,>=,=,==,!='
'''print(3<4,4>3)
print(3<=4,4<=4,5<0.1)
print(3>=4,4>=4,5>0.1)
print('hai'=='hai','hai'=='hi')
print('hai'!='hai','hai'!='hi')
print(3>4,5>0.1)
print('hai'!='hai','hai'!='bye')'''
#3.logical operator
#i)or---->this operator returns true if one condition will be correct
'''print(45<45 or 45>=45)
print(20>30 or 30<50)'''
#ii)and--->this return true if both statement or condition is true
'''print(1<5 and 6<4)
print(4>1 and 3>2)'''
#iii)not--->reverse the result,return  false if the result is true
'''print(not(5>3 and 5<10))
print(not(5>3 and 5>2))'''

#4.bitwise operator
#i)or--->'|'convert the number to binary then perform the or opertaion
'''n1=34
n2=40
print(n1|n2)
n3=5
print(n1|n2|n3)'''
#ii)and--->'&'
'''n1=34
n2=40
print(n1&n2)
n3=62
print(n1&n2&n3)'''
#iii)not--->'-'
'''print(34)
print(-40)'''
#iv)xor--->'^'
#same operator-->0     different operator---->1
'''n1=45
n2=40
print(n1^n2)
n3=20
n4=20
print(n3^n4)'''

#5.assignment operator
#i)=
'''n=89
print(n)
#ii)+
n=n+1
n+=10
print(n)
#iii)*
n='hi'
n*=4
print(n)
#iv)/
n=9
n/=3
print(n)
#v)%=
n=34
n%=2
print(n)
#vi)-=
n=34
n-=2
print(n)
#vii)**
n=34
n**=8
print(n)
#viii)//=
n=8
n//=2
print(n)'''

#6.identity operator
#i)is--->to check the address is same
'''print(10==10)
n=20
n1=20
print(n is n1)'''
#ii)is not--->to check the address is different
'''n2=45
n3='hey'
print(n2 is not n3)'''

#7.membership operator
#i)in
'''print('h' in 'hai','H' in 'hai')
print('h'=='hai')
print('bye' in ['hai','hello','bye'])
print('bye' in {'hai':3,'hello':45,'bye':4.5})'''
#ii)not in
'''print(45 not in {'hai':3,'hello':45,'bye':4.5})
print('hai' not in {'hai':3,'hello':45,'bye':4.5})'''
