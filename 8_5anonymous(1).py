#anonymous function
#1.program to square a number
'''square_=lambda num:num*num
print(square_(4))'''

#2.program to find the square and cube
'''square_=lambda num:(num*num,num**3)
print(square_(4))'''

#3.program to cheack a character is vowel or not
'''vowel_not=lambda vow:vow in 'aeiouAEIOU'
print(vowel_not('a'))'''

#4.program to check a number is even or not
'''num_=lambda n:n%2==0
print(num_(4))'''

'''num_=lambda n:n in (2,4,6,8,10)
print(num_(5))'''

#5.write a python program to create a lambda function
#that add 15 to a given number
'''n_=lambda n:n+15
print(n_(2))'''

#6.create lambda function that multiplies 2 arguments
'''n_=lambda a,b:a*b
print(n_(2,3))'''

#7.program to add two numbers
'''n_=lambda a,b:a+b
print(n_(2,3))'''

#8.program to solve a**2+b**2+2*a*b
'''n_=lambda a,b:a**2+b**2+2*a*b
print(n_(2,3))'''

#9.program to solve 2*a+3*b+4*c
'''n_=lambda a,b,c:2*a+3*b+4*c
print(n_(4,5,2))'''

#10.program to return last data of any sequence
'''seq_=lambda n:n[-1]
print(seq_('rsdgfhbj'))
print(seq_([1,2,34,5]))'''

#11.program to check if a string is palindrome or not
'''pal_no=lambda n:n==n[::-1]
print(pal_no("kok"))'''

#12.program to negative to positive number
'''neg_pos=lambda n:abs(n)
print(neg_pos(-2))'''

#13.check a data is present in a list
'''lst=[1,2,3,4,5,6]
num=lambda lst,n:n in lst
print(num(lst,4))'''

#15.program to get all vowels in string
'''s_v=lambda s:[char for char in s if char in 'aeiou']
print(s_v('hello world'))'''

#16.check if string length is more than 5
'''str_=lambda s:len(s)>5
print(str_('hel!'))'''

#17.
