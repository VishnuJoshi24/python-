def evenOdd():
    n=int(input('enter the no'))
    if(n%2==0):
        print('its even')
    else:
        print('its odd')
          
def world():
    print("hello world")
    
def pattern():
    for i in range(1,6):
        for j in range(1,i+1):
            print(i,end= ' ')
        print()
def sumOfNum():
    n=int(input("enter a number"))
    sum=0
    for i in range(1,n):
        sum+=i
    print("sum=",sum)
     
def multiples():
    for i in range(1,11):
        print(i,"10 = ",i*10)

evenOdd()
world()
pattern()
sumOfNum()
multiples()
    
    
