#1)
'''
*
* *
* * *
* * * *
* * * * *'''
'''for n in range(1,6):
    print(n * '*')'''
#2)
'''
* * * * * *
* * * * *
* * * *
* * *
* *
*'''
'''for n in range(6,0,-1):
    print('*' * n)'''
#3)
'''
           *
        * *
      * * *
   * * * *
* * * * * '''
'''for n in range(1,6):
    print(f"{n *' *':>15}")'''
#4)
'''
       *      
      * *      
     * * *     
    * * * *      
   * * * * *    '''
'''for n in range(1,6):
    print(f"{n * ' *':^15}")'''

#5)
'''
    * * * * * *
      * * * * *
        * * * *
          * * *
            * *
              *   '''
'''for n in range(6,0,-1):
    print(f"{n * ' *':>15}")'''

#6)
'''
  * * * * *   
    * * * *    
     * * *     
      * *      
       *    '''
'''for n in range(5,0,-1):
    print(f"{n* ' *':^15}")'''

#7)
'''
1 
 1 2 
 1 2 3 
 1 2 3 4 
 1 2 3 4 5 
'''
'''str_=' '
for i in range(1,6):
    str_+=str(i)+' '
    print(str_)'''
#8)
'''str_=' '
for i in range(1,6):
    str_+=str(i)+' '
    print(str_)'''
#9)
'''
 A 
 A B 
 A B C 
 A B C D 
 A B C D E'''
'''str_=' '
l_='A','B','C','D','E'
for i in range(0,5):
    str_+=l_[i]+' '
    print(str_)'''

'''str_=' '
for ascii_v in range(ord('A'),ord('F')):
    str_+=chr(ascii_v)+' '
    print(str_)'''
#10)
'''
 *
 *
 *
 * *
 *
 * * *
 *
 * * * *
 *
 * * * * * '''
'''for i in range(1,6):
    print(' *')
    print(i*' *')'''

#11)
'''
//str_=' '
l_='A','B','C','D','E'
for i in range(5,0,-1):
    for j in range(i):
        str_=chr(ord('a')+j)
        print(str_,end=' ')
    print()'''#go to next line(\n)
    #i--->(5,1)--->5,4,3,2,1
    #j---->(0,4)--->j=0,1,2,....
    #str_=chr(ord('a')+j)
         #chr(ord(65))+0--> o/p :a..
    
    
