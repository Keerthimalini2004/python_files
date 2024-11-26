#3.write a python program to get sum of the even numbers in the range
'''even_num=sum(filter(lambda x:x%2==0,range(1,11)))
print(even_num)'''

'''even_num=sum([n for n in range(1,11) if n%2==0])
print(even_num)'''
#4.write a program to cheack whether the given number is special number or not
'''n=int(input("enter the number:"))
a=str(n)
s=0
m=1
for digit in a:
    s+=int(digit)
    m*=int(digit)
j=s+m
if j==n:
    print("special character")
else:
    print("not a specail character")'''

'''def spe_num(num):
    sum_=sum([int(i) for i in str(num)])
    p=1
    for i in str(num):
        p*=int(i)
    if sum_+p==num:
        return"special num"
    else:
        return "not a special num"
print(spe_num(29))'''

#5.program to print multiplication table to the given numbers in a range
'''def mul_table(n):
    for j in range(1,n+1):
        for i in range(1,n+1):
            print(j,'*',i,'=',j*i)
num=int(input("enter the number:"))
mul_table(num)'''

'''n=int(input("enter the number:"))
for i in range(1,10):
    print(n,'*',i,'=',n*i)'''

#6.check whether the number is neon number or not
'''n=int(input("enter the number:"))
a=n**2
b=str(a)
s=0
for digit in b:
    s+=int(digit)
if n==s:
    print("the given number is neon")
else:
    print("it is not possible")'''

'''def neon_num(n=int(input("enter the number:"))):
    a=n**2
    b=str(a)
    s=0
    for digit in b:
        s+=int(digit)
    if n==s:
        return "the given number is neon"
    else:
        return "it is not possible"
print(neon_num(9))'''
#7.write a python program to find the factors of a given number
'''n=int(input("enter the number:"))
l=[]
for i in range(1,n+1):
    if n%i==0:
        l.append(i)
print(l)  '''

'''def factors_(n):
    l=[]
    for i in range(1,n+1):
        if n%i==0:
            l.append(i)
    return(l)
print(factors_(10))'''

#8.Xylem
'''n=int(input("enter the number:"))
a=str(n)
s=int(a[0])+int(a[-1])
inner_digit=sum([int(i) for i in a[1:-1]])
print(s,inner_digit)
if s>inner_digit:
    print("Xylem")
else:
    print("Phloem")'''

'''def xy_ph_num(n):
    num_=str(n)
    outer_digit=int(num_[0])+int(num_[1])
    inner_digit=sum([int(i) for i in num_[1:-1]])
    print(outer_digit,inner_digit)

    if len(num_)<=2:
        print(f' The {num_} is not both Xylem and Phloem')
    elif outer_digit>inner_digit:
        print(f' {num_} is Xylem')
    elif outer_digit<inner_digit:
        print(f' {num_} is phloem')
    else:
        print("the sum of inner and outer numberrs are same")

xy_ph_num(3456)
xy_ph_num(8336)'''

#9.write a program to find the sum of factors of a given numbers
'''def factors_(n):
    l=[]
    for i in range(1,n+1):
        if n%i==0:
            l.append(i)
    return(l)
print(factors_(10))
print(sum(factors_(10)))'''

#10.write a program to print GCD inbetween two numbers
'''def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

num1=int(input("enter the number1:"))
num2=int(input("enter the number2:"))
gcd_value=gcd(num1,num2)
print(gcd_value)'''

#11.write a program to check whether the given number is
#strong number or not(145=1fac+4fac+5fac)=145)




                                                            #-------pattern program-------
#1.
'''               A
                BAB
             CBABC
          DCBABCD
        EDCBABCDE '''

'''n=int(input("enter:"))
sp=n-1
stars=1
dummy=1
for i in range(n):
    dummy=i+65
    for s in range(sp):
        print(' ',end=' ')
    for d in range(stars):
        print(chr(dummy),end=' ')
        if d<stars//2:
            dummy-=1
        else:
            dummy+=1
    sp-=1
    stars+=2
    print()'''
            
#2.
'''
    * 
   * * 
  * * * 
 * * * * 
* * * * * '''

'''n=5
for i in range(1,n+1):
    print(' '*(n-i)+'* '*i)
    '    '+'*'*1'''#4 spaces leaves from margin
 
'''n=int(input('enter:'))
for i in range(n):
    for l in range(i,-1,-1):
        print(chr(65+l),end=' ')

    for r in range(1,i+1):
        print(chr(65+r),end=' ')'''

#1.A  j-->is column / i--->is row
'''
* * * * *
*          *
* * * * *
*          *
*           * '''
'''n=5
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or j==n-1:
            print('*',end=' ')
        elif i==2:
            print('*',end=' ')
        else:
            print('  ',end=' ')
    print()'''

#2.B
'''
* * * * * 
*          * 
* * * * * 
*          * 
* * * * * 
'''
'''n=5
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or j==n-1:
            print('*',end=' ')
        elif i==2 or i==4:
            print('*',end=' ')
        else:
            print('  ',end=' ')
    print()'''

#3.C
'''
* * * * * 
*             
*             
*             
* * * * *
'''
'''n=5
for i in range(n):
    for j in range(n):
        if i==0 or j==0:
            print('*',end=' ')
        elif i==4:
            print('*',end=' ')
        else:
            print('  ',end=' ')
    print()'''

#4.D
'''
* * * * * 
*          * 
*          * 
*          * 
* * * * * '''
'''n=5
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or j==n-1:
            print('*',end=' ')
        elif i==4:
            print('*',end=' ')
        else:
            print('  ',end=' ')
    print()'''

#5.E
'''
* * * * * 
*             
* * * * * 
*             
* * * * * '''
'''n=5
for i in range(n):
    for j in range(n):
        if i==0 or j==0:
            print('*',end=' ')
        elif i==4 or i==2:
            print('*',end=' ')
        else:
            print('  ',end=' ')
    print()'''

#6.F
'''
* * * * * 
*             
* * * * * 
*             
*  '''
'''n=5
for i in range(n):
    for j in range(n):
        if i==0 or j==0:
            print('*',end=' ')
        elif i==2:
            print('*',end=' ')
        else:
            print('  ',end=' ')
    print()'''

#7.G
'''
* * * * * 
*             
*    * * * 
*    *    * 
* * *    * '''
'''n=5
for i in range(n):
    for j in range(n):
        if i==0 or j==0:
            print('*',end=' ')
        elif (i==2 and j==2) or (i==2 and j==3):
            print('*',end=' ')
        elif i==2 and j==4:
            print('*',end=' ')
        elif (i==3 and j==2) or (i==3 and j==4):
            print('*',end=' ')
        elif (i==4 and j==1) or (i==4 and j==4) or (i==4 and j==2):
            print('*',end=' ')
        else:
            print('  ',end=' ')
    print()'''

#8.H
'''
*          * 
*          * 
* * * * * 
*          * 
*          *'''
'''n=5
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1:
            print('*',end=' ')
        elif i==2:
            print('*',end=' ')
        else:
            print('  ',end=' ')
    print()'''
#9.I
'''
* * * * * 
      *       
      *       
      *       
* * * * *
        '''
'''
n=5
for i in range(n):
    for j in range(n):
        if i==0:
            print('*',end=' ')
        elif i==4:
            print('*',end=' ')
        elif j==2:
            print('*',end=' ')
        else:
            print('  ',end=' ')
    print()'''
#10.J
'''
* * * * * 
      *       
      *       
*    *       
* * *    '''
'''
n=5
for i in range(n):
    for j in range(n):
        if i==0 or j==2:
            print('*',end=' ')
        elif (i==4 and j==1):
            print('*',end=' ')
        elif (i==3 and j==0):
            print('*',end=' ')
        elif (i==4 and j==0):
            print('*',end=' ')
        else:
            print('  ',end=' ')
    print()'''
#11.K
'''
*          * 
*    *       
*             
*    *       
*          * '''
'''
n=5
for i in range(n):
    for j in range(n):
        if j==0:
            print('*',end=' ')
        elif (i==1 and j==2) or (i==0 and j==4) :
            print('*',end=' ')
        elif (i==3 and j==2) or (i==4 and j==4) :
            print('*',end=' ')
        else:
            print('  ',end=' ')
    print()'''
#12.L
'''
*             
*             
*             
*             
* * * * * 
'''
'''n=5
for i in range(n):
    for j in range(n):
        if j==0:
            print('*',end=' ')
        elif i==4:
            print('*',end=' ')
        else:
            print('  ',end=' ')
    print()'''

#13.M
'''
*          * 
* *    * * 
*    *    * 
*          * 
*          * '''
'''
n=5
for i in range(n):
    for j in range(n):
        if j==4 or j==0:
            print('*',end=' ')
        elif (i==1 and j==1) or (i==2 and j==2) or (i==1 and j==3) :
            print('*',end=' ')
        else:
            print('  ',end=' ')
    print()'''
#14.N
'''
*          * 
* *       * 
*    *    * 
*       * * 
*          * '''
'''
n=5
for row in range(n):
    for col in range(n):
        if col==0 or col==4:
            print('*',end=' ')
        elif (col==1 and row==1) or (col==2 and row==2) or (col==3 and row==3):
            print('*',end=' ')
        else:
            print('  ',end=' ')
    print()'''
#15.O
'''n=5
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or j==n-1:
            print('*',end=' ')
        elif i==4:
            print('*',end=' ')
        else:
            print('  ',end=' ')
    print()'''
#16.P
'''
* * * * * 
*          * 
* * * * * 
*             
*'''
'''n=5
for i in range(n):
    for j in range(n):
        if i==0 or j==0:
            print('*',end=' ')
        elif i==2:
            print('*',end=' ')
        elif i==1 and j==4:
            print('*',end=' ')
        else:
            print('  ',end=' ')
    print()'''

#17.Q

#18.R
'''n=5
for i in range(n):
    for j in range(n):
        if i==0 or j==0:
            print('*',end=' ')
        elif i==2:
            print('*',end=' ')
        elif i==1 and j==4:
            print('*',end=' ')
        elif i==3 and j==2 or i==4 and j==3:
            print('*',end=' ')
        else:
            print('  ',end=' ')
    print()'''

#19.09.24
#1.i/p=4 & o/p={1,2,3,4} (add 1st and last index&add 2nd and last previous index)
'''n=int(input("enter the nuber:"))
s_=set()
for i in range(1,n+1):
    s_.add(i)

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

l_=list(s_)
print(gcd(l_[0],l_[-1])+gcd(l_[1],l_[2]))'''

#2.write a prgm to get nth fibonacci number(in note explanation)
'''def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
print(fib(7))
print(fib(10))'''

'''num=int(input("enter the number:"))
a=0
b=1
print(a)
print(b)
for i in range(2,num+1):
    c=a+b
    a=b
    b=c
    print(c)'''

#3.write a prgm to create a recursion function for power of a number
'''def pow(a,b):
    m=a**b
    print(m)
pow(3,2)'''

'''def pow(a,b):
    if a<=0 or b<=0:
        return 0
    else:
        return a**b
print(pow(3,2))
print(pow(-4,5))
print(pow(4,5))'''

#in recursion
'''def pow(base,exp):
    if exp<=0:
        return 1
    return base*pow(base,exp-1)
print(pow(2,4))'''

#4.write a recursion function to count number of digits

#5.write a recursion function to get the triangular number
#eg : i/p=5 then sum from 5,4,3,2,1 until one
'''s=0
def Sum(n):
    if n>0:
        for i in range(1,n+1):
            su_=s+i
            print(su_)
    else:
        return 1
print(Sum(5))'''
#done by mam
'''def triangular_number(n):
    if n<=1:
        return 1
    return n+triangular_number(n-1)

print(triangular_number(5))
print(triangular_number(10))'''







