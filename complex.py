#complex
'''c1,c2=4+34j,3.4-4.5j
print(c1,c2)'''

#constructor
'''#1.
print(complex())
#2.typecasting
#int-->complex
print(complex(45), complex(45j))
#float-->complex
print(complex(34.5), complex(45.6j))
#bool--->complex
print(complex(True))
#string-->complex
print(complex('90j'),
            complex('4.5'),
             complex('4'))'''

#operators in complex
'''n1=complex(input("enter the 1st num:"))
n2=complex(input("enter the 2nd num:"))
print("addition:",n1+n2)
print("sub:",n1-n2)
print("mul:",n1*n2)
print("div:",n1/n2)
print("expo",n1**n2)'''

#4.boolean
b1,b2=True,False
print(b1,b2)
print(type(b2))
#constructor
#1.
'''print(bool())
#note
print(bool(0),bool(54))
print(bool(0.0),bool(54.8))
print(bool(0j),bool(34+3j))
print(bool(False),bool(True))'''

#user input
#string
'''i=bool(input("enter:"))
print(i,type(i))
#integer
i=bool(int(input("enter:")))
print(i,type(i))
#float
i=bool(float(input("enter:")))
print(i,type(i))
#complex
i=bool(complex(input("enter:")))
print(i,type(i))'''







