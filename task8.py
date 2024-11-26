#1)find the highest score in a set of scores.take the score from the user input.
#i)get the output with method.
'''scores_={32,54,6,78,2}
print(max(scores_))'''
#ii)get the output without method
'''scores_=input("enter ur score:").split(' ')
max_scr=0
for num in scores_:
    if int(num)>max_scr:
        max_scr=int(num)
print(max_scr)'''

#2)#2.average
#with method
'''heights={45,32,6,73,43}
sum_=sum(heights)
count_=len(heights)
print(f'the average:{sum_//count_}')'''
#without method
'''heights={45,32,6,73,43}
sum_,len_=0,0
for height in heights:
    sum_+=height
    len_+=1
print(f'the average:{sum_//len_}')'''

#3)write a program to get fizzbuzz number
'''num_=int(input("enter the number:"))
i=1
while i<n:
    if i%3==0:
        print("fizz")
    elif num_%5==0:
        print("buzz")
    elif num_%5==0 and num_%3==0:
        print("fizzbuzz")
    else:
        print(num_,"is invalid")
    i+=1'''

'''num_=int(input("enter the number:"))
for i in range(0,num_):
    if i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    elif i%5==0 and i%3==0:
        print("fizzbuzz")
    else:
        print(i,"is invalid")'''

'''num_=int(input("enter the number:"))
if num_%3==0:
    print("fizz")
elif num_%5==0:
    print("buzz")
elif num_%5==0 and num_%3==0:
    print("fizzbuzz")
else:
    print(num_,"is invalid")'''
#4)password generator(not done)
'''alphabets=int(input("enter the alpathabets you need?:"))
numbers=int(input("enter the numbers you need?:"))
special_char=int(input("enter the special char you need?:"))

alpha_=' '
for a in range(ord('a'),ord('z')+1):
    if chr(a).isalpha():
        alpha_+=chr(a)
    print(alpha_)

numbers_=' '
for num in range(0,10):
    numbers_+=str(num)
#print(numbers_)

special_char_='!@#$%^&*()'
password_=' '
for _ in range(1,alphabets+1):
    password_=password_+choice(alpha_)

for _ in range(1,numbers+1):
    password_=password_+choice(numbers_)

for _ in  range(1,special_char_+1):
    password_=password_+choice(special_char)

shuffeld_password=''.join(set(password_))
print("gerate a password is:",{shuffeld_password})'''


#5)grading system project
'''marks_=int(input("enter the mark of the student:"))
if marks_>80:
    print(marks_,"mark is Grade A")
elif marks_>60 and marks_<=80:
    print(marks_,"mark is Grade B")
elif marks_>50 and marks_<=60:
    print(marks_,"mark is Grade C")
elif marks_>45 and marks_<=50:
    print(marks_,"mark is Grade D")
elif marks_>25 and marks_<=45:
    print(marks_,"mark is Grade E")
else:
    print(marks_,"mark is Grade F")'''

#6)
'''a=int(input("no.of classes held:"))
b=int(input("no.of classes attended:"))
attend_=b/a*100
print("percentage of class attended is:",attend_)
if attend_>=75:
    print("the student is allowed to sit")
else:
    print("the student is not allowed to sit")'''


