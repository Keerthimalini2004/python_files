#decision making
#i)if condition
'''if True:
    print('hai')
if False:
    print('hai')
if bool(1):
    print('bye')
if bool(0):
    print('bye')'''
#2.
'''if bool(0) or bool(1):
    print('bye')
if bool(0) and bool(1):
    print('bye')'''

'''n=input("enter:")
if n:
    print('data is present')
print('data is not present')'''

#ii)if else condition
'''n=input("enter:")
if n:
    print('data is present')
else:
    print('data is not present')'''

#iii)nested if condition
#1.
'''if True:
    print('main if')
    if True:
        print('nested if')
    else:
        print('nested else')
else:
    print('main else')'''

#2.
'''if False:
    print('main if')
    if False:
        print('nested if')
    else:
        print('nested else')
else:
    print('main else')'''

#iv)elif condition
#1.
'''if False:
    print('A')

elif False:
    print('B')

elif False:
    print('C')

else:
    print(False)'''
#2.
if False:
    print('A')

elif True:
    print('B')

elif False:
    print('C')

else:
    print(False)

#write a program to chech a character is vowel or not
    #1.own
'''a=input("enter a character:")
vowels_='a','e','i','o','u'
if (a==a):
    print("a is a vowel")
elif(a==e):
    print("e is a vowel")
elif(a==i):
    print("e is a vowel")
elif(a==o):
    print("o is a vowel")
else:
    print("no match")'''
#2.
'''
a=input("enter a character:")
vowels_='a','e','i','o','u'
if a in vowels_: 
    print("vowels are matched")
else:
    print("no match")'''
