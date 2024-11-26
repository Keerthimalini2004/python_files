#convention for variable#not work
'''mynameis='ashwini'
print(mynameis)                             
#pascal case--->classname
MyNameIs='Ashwini'
print(MyNameIS)
#camel case--->methodname
myNameIs='Ashwini'
print(myNameIs)
#snake case--->functionname
my_name_is='Ashwini'
print(my_name_is)'''

#welcome-->reverse and skip odd index
str2="welcome to my channel"
print(str2[-2::-2])
'''print(str2[-15:-22:-2])
print(str2[6::-2])
#skip odd index char
print(str2[0:21:2])
#to my-->reverse and skip even index
print(str2[-9:-14:-2])
print(str2[13:7:-2])'''

#string is immutable(exception)
'''str4='hello worls'
str4[0] = 'h'
print(str4)'''
#------------------------------*----------------------------------------------
#method in string
'''str1='hello world '
print(str1.replace('l','L'))
print(str1.replace('hello','hai'))
print(str1.replace('l','L',1))
print(str1)
print(str1.replace('o','@',2))
#exception
print(str1.replace('heoll','hai'))'''

#2.lower
'''s2=input("enter the string:")
print(s2.lower())

#3.upper
s3=input("enter the string:")
print(s3.upper())'''

#4.swapcase
'''s3=input("enter the string:")
print(s3.swapcase())'''

#5.islower()
'''s3=input("enter the string:")
print(s3.islower())
#6.isupper()
print(s3.isupper())'''

#isalpha
'''s3=input("enter the string:")
print(s3.isalpha())
#isnumeric
print(s3.isnumeric())'''

#isalnum
'''s3=input("enter the string:")
print(s3.isalnum())
#isspace
print(s3.isspace())'''

#startwith
'''str1="Tamil Nadu"
sub=input("substring:")
print(str1.endswith(sub))
sub=input("substring:")
end=int(input("end:"))
print(str1.endswith(sub,0,end))'''

#index
str1="Tamil Nadu"
sub=input("substring:")
print(str1.index(sub))
sub=input("substring:")
ind=int(input())
print(str1.index(sub,ind))



