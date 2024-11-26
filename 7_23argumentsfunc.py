#types of arguments
#1)positional arguments
'''def f1(name,age,id):
    return name,age,id


print(f1('keerthi',20,31))'''

#2)keyword argument
'''def func(name,age):
    print(name,age)


func(age=23,name="neha")'''

#3)combination of positional and keyword arguments
'''def f1(name,age,id):
    print(name,age,id)
    
f1('rani',age=34,id=3)'''

#4)only positional and keyword argument
#i)only positional argument
'''def f1(a,b,/,c,d):
    print(a,b,c,d)
f1(10,20,c=45,d=87)
f1(10,20,45,87)
f1(10,20,45,d=87)
#exception
f1(10,b=20,c=45,d=87)'''

#ii)only keyword argument
'''def f1(a,b,*,c,d):
    print(a,b,c,d)

    
f1(a=10,b=34,c=45,d=86)
f1(10,45,c=45,d=76)
f1(10,b=43,c=65,d=89)'''

#5)variable positional arguments
'''def func(*args):
    print(args)

func(3,4,5)
func('hai',[4,5,6],True)'''

#6)varible keyword argument
'''def func(**kwargs):
    print(kwargs)

func(a=54,b=4.5,c=False,d='python',e=[False,True])'''

def func(string,*args,**kwargs):
    print("\n",string,"\n",args,"\n",kwargs)
func(34,5,6,c=False,d='python',e=[False,True])
          



#the task for this in (task7args)
