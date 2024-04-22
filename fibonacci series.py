#fibonacci series
def fib(i):
    if i==0:
        return 0
    elif i==1:
        return 1
    else:
        return(fib(i-1)+fib(i-2))
    
i=int(input('enter the limit'))
print('fibonacci series',end=' ')
for i in range(0,i):
    print(fib(i),end=' ')
print()
print()
################################################
    
a=0
b=1
i=int(input('enter the limit'))
print('fibonacci series',a,b,end=' ')
for i in range(3,i+1):
    c=a+b
    print(c,end=' ')
    a=b
    b=c
    