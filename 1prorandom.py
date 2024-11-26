#random example
'''import random
print(random.randint(1,20))'''
#2.eg(error)
'''l_=[4,4.5,12,67]
index_=random.randint(a:0,len(l_)-1)
print(l_[index_],'at the index',index_)'''

#choice
'''import random
places=['goa','varkala','karnataka','AP']
print('lets visit',random.choice(places))'''

#1.program to get tail or head
'''import random
num_=random.randint(0,1)
if num_==1:
    print('head')
else:
    print('tail')'''

#2.program to guess a number
import random
'''name=input("what is your name:")
print("hay",name,"lets start the game")
computer_guess=random.choice((1,2,3,4,5,6,7,8,9,10))
user_guess=int(input("Guess a number:1 to 10"))
print(computer_guess)
if user_guess==computer_guess:
    print("you win")
elif user_guess<computer_guess:
    print("guess larger number")
elif user_guess>computer_guess:
    print("guess lower number")
else:
    print("guess only number in the tuple")'''

#3.program stone, paper and scissor
'''import random
name=input("what is your name:")
print("hey",name,"lets start the game")
computer_item=random.choice(['scissor','stone','paper'])
user_input=input("user input is scissor or rock or paper:")
print("computer guess:",computer_item)
if computer_item==user_input:
    print('draw')
elif  computer_item=='scissor':
    if user_input=='rock':
        print("you won rock hits scissor")
    else:
        print("you lost scissor cuts the paper")

elif computer_item=='rock':
    if user_input=='paper':
        print("you won paper wrap the rock")
    else:
        print("you lost rock hits the scisssor")
        
else:
    if user_input=='scissor':
        print("you won scissor cuts the paper")
    else:
        print("you lost paper wrap the rock")'''

#4.
'''mark=int(input("enter the mark:"))
if mark>=80:
    print("Grade A")
elif mark<80 and mark>=60:
    print("Grade B")
elif mark<60 and mark>=50:
    print("Grade C")
elif mark<50 and mark>=45:
    print("Grade D")
elif mark<45 and mark>=25:
    print("Grade E")
else:
    print("Grade F")'''

#5.i)take input of age of 3 people by user and determine oldest among them
'''a1=int(input("enter the age:"))
a2=int(input("enter the age:"))
a3=int(input("enter the age:"))
if a1>a2 and a1>a3:
       print("a1 is oldest")
elif a2>a1 and a2>a3:
       print("a2 is oldest")
else:
    print("a3 is oldest")'''
        
#ii)take input of age of 3 people by user and determine o among them
'''a1=int(input("enter the age:"))
a2=int(input("enter the age:"))
a3=int(input("enter the age:"))
if a1<a2 and a1<a3:
       print("a1 is youngest")
elif a2<a1 and a2<a3:
       print("a2 is youngest")
else:
    print("a3 is youngest")'''

#if the person attendance is leass than 75 not allowed to sit in class
name=input("enter the name of the student:")
tot_class=int(input("total number of class:"))
present=int(input("enter the attendence:"))
per_=present/tot_class*100
print(per_)
if per_<75:
    print("not allowed to sit in the class")
else:
    print("allowed to sit in the class")

       
