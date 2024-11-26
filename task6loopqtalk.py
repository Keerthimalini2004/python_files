#1)program to check a number is prime or not(important)
'''number=int(input("enter the number:"))
for n in range(2,number): #2,3,4,5-->2,3,4
    if number%n==0:#5%2==1
        print("it is not a prime number")
        break
else:
    print("it is a prime number")'''

#2)to get prime numbers in a range(important)
'''start_value=int(input("enter the number:"))
end_value=int(input("enter the number:"))
for i in range(start_value,end_value+1):
    for j in range(2,i):
        if i%j==0:
           break
    else:
        print(i)'''

#ii)
'''start_value=int(input("enter the number:"))
end_value=int(input("enter the number:"))
for i in range(start_value,end_value+1):
    if i<=1:
        pass
    else:
        for j in range(2,i):
            if i%j==0:
               break
        else:
               print(i,end=' ')'''

#3)program to get factorial of a number
'''a=int(input("enter a number:"))
fact_=1
for i in range(fact_,a+1):
    fact_=fact_*i
print(fact_)'''

#4)program to print fibanocci series#0112358
'''num1=int(input("enter the number:"))
a=0
b=1
if num1<=1:
    print(0)
else:
    print(a)#0
    print(b)#1
for i in range(2,num1):#(2,5)-->2,3,4-->2
    c=a+b#0+1=1|o+
    a=b#a=1
    b=c#b=1
    print(c)#1
    '''

#5)program to check armstrong number
'''num=int(input("enter the number:"))
l=len(str(num))
sum_=0
for digit in str(num):
    sum_+=int(digit)**l
if sum_==numprint(num,"is a armstrong number")
else:
    print(num,"is not a armstrong number")'''

#6)
'''in_=input("enter the filename:").split('.')
print(in_[-1])'''
#qtalk loop pdf task
#2)sum of 1st 10 natural numbers
'''i=1
while i<=10:
    n=i*(i+1)/2
    i+=1
print(n)
'''
#3)to get only even numbers from 1 to 20
'''for i in range(1,21):
    if i%2==0:
        print(i)'''

#4)program to reverse a given number
'''num=input("enter the number:")
i=0
while i<len(num):
    i+=1
print(num[::-1])'''

#5)check a number is prime(some mistake)
'''num=int(input("enter the number:"))
i=2
while (i<num):
    if num/i==0:
        print(num,"not a prime")
        break
    i+=1
else:
    print(num,"it is prime")'''

#6)print fibonacci series
'''num=int(input("enter the number:"))
a=0
b=1
if num<=1:
    print(o)
else:
    print(a)
    print(b)
for i in range (2,num):
    c=a+b
    a=b
    b=c
    print(c)'''

#13)
num_=int(input("enter the number"))
i=0
sum1=0
while i<=num:
    num_=i*i
    print(num_)
    sum1+=num_[i]
    i+=1
print(sum1)
        
