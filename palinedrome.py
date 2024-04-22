# to check palinedrome
num=int(input('enter the num'))
temp=num
rev=0
rem=0
while num>0:
    
    rem=num%10
    rev=(rev*10)+rem
    num//=10
if temp==rev:
    print(rev,'is palindrome')
else:
    print(rev,'is not palindrome')