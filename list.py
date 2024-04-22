#LIST

#LIST does have fixed size,it can be variable
#in list single index can contain multiple values
#List can be mutable
#it can have different type of dataType

apple=[10,5,30,60,100,45,50]
print(apple)
print(apple[1])
print(apple[-1])
print(apple[-3])
print(apple[1:4])  #traversing
print(apple[:])    #travers completly
print(apple[-4:-1])
print(apple[2:-1])
print(apple[:-1])
print(apple[0:])
print(apple[0:7:3])

print()

'''a[3]=(20,30)
print(apple)'''


print('for itration via access elements')
for i in apple:
    print(i,end=' ')
print()
    
print('after change')
apple=[10,-100,30]
print(apple)
print()

banana=[10,2.003,'abc']
print(banana)
print()
print()

#concatenate list
ls1=[1,2,3,4]
ls2=[5,6,7,8]
list3=ls1+ls2
print(list3)
print(type(list3))
# repeat list
print(ls1*2)
print(len(ls1))
print(max(ls2))
print(min(ls2))

#addition of ele in list
ls1=[10,20,15,17,25,27]
sum=0
for i in ls1:
    sum+=i
    if i%10==7:
        print(i,end=' ')
print('sum=',sum)

#To remove duplication





for i in range(-10,10,2):
    print(i+1)



#LIST using USER INPUT

ls=[]
n=int(input('enter the size '))
for i in range(0,n):
    ele=int(input('enter the elements'))
    ls.append(ele)
print(ls)

#used to store common ele in lnew list 
nagaraj=[]
n=int(input('enter the size'))
for i in range(0,n):
    ele=int(input('enter the elements'))
    nagaraj.append(ele)

yuraj=[]
n=int(input('enter the size'))
for i in range(0,n):
    ele=int(input('enter the elements'))
    yuraj.append(ele)
dup=[]  
for i in yuraj:
    if i in nagaraj:
        dup.append(i)
print(dup)
    
    
        
        
        
'''5 value from user find which num r prime num and leap year 2000,10,85,1996,17'''
