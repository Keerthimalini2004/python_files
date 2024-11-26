
'''
print(s4)
print(type(s4))'''

#constructor
#   1.
'''print(str())'''

#2.typecasting
'''i,f,c,w=str(34),str(3.4),str(3+4j),str(False)
print(type(i),i)
print(type(f),f)
print(type(c),c)
print(type(w),w)'''

#to know no of characters
'''s_=input("Enter the string:")
print("string:",s_,
     "its length is:",len(s_))'''

'''str1="B@ng@!0r3"
print(id(str1))
#indexing
print(str1,len(str1))
#starting character
print(str1[0], str1[-9], str1[-len(str1)])
#ending character
print(str1[8],str1[len(str1)-1],str1[-1])
#to get the id and the character are same the address is same
print(id(str1[1]),id(str1[4]))
#to get the middle character
print(str1[5],str1[len(str1)-5],str1[-len(str1)])
#practical way
str2=input("enter:")
middle_index=len(str2)//2 #single / gives float  value so floor division is used
print(middle_index,str1[middle_index])'''

#to get the last 2 character
'''s1=input("Enter a string:")
last_sec=len(s1)-2
print(s1[last_sec])
#2.
print(s1[-2])'''

#2.slicing
'''s2="it's cold here"
print(s2,s2[::],s2[0:len(s2):1])

#it's
print(len(s2))
print(s2[0:4:1],
         s2[:4:],
          s2[-len(s2):-10:1])
#here
print(s2[-4::],
      s2[10::])
#cold
print(s2[5:9:],
      s2[-9:-5:])'''

#date 18.06.24
#when the step value is more than 1 for even put 0 at start
'''s3=''welcome to my channel''
print(s3)
print(s3[0:len(s3):2])
print(s3[::2])
#when the step value is more than 1 for odd put 1 at start
print(s3[1:len(s3):2])
print(s3[1::2])

#welcome
print(s3[:7:])
print(s3[:7:2])#welcome skip odd index char
print(s3[1:7:2])#welcome skip even index char
'''

#reversing the string
s4="welcome to my channel"
'''print(s4[::-1])
print(s4[len(s4):-len(s4)-1:-1])

#channel
print(len(s4))
print(s4[len(s4):-8:-1])
print(s4[-1:-8:-1])

#welcome to
print(s4[-12:-22:-1])#negative index
print(s4[9::-1])#positive index'''

#to my
'''print(s4[-9:-14:-1])
print(s4[12:7:-1])'''

#task 1
'''str1="slicing is tricky"
print(len(str1))
#ing is tr
print(str1[12:3:-1])#positive index
print(str1[-5:-14:-1])#negative index
#slicing
print(str1[6::-1])#positive index
print(str1[-11:-18:-1])#negative index
#is tricky
print(str1[16:7:-1])#positive index
print(str1[-1:-10:-1])#negative index'''



str1="welcome to the world"
print(str1[3:10:1])
print(str1[-17:-10:1])
print(str1[9:2:-1])
print(str1[-11:-18:-1])
print(str1[-1:-13:-2])
print(str1[len(str1)-1:7:-2])




