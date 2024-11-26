#1.max number
#with method
'''t_={34,5,6,2,76}
print(max(t_))'''
#without method
'''numbers=input("enter some numbers:").split()
max_num=0
for num in numbers:
    if int(num)>max_num:
        max_num=int(num)
print(max_num)'''

#2.average
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


