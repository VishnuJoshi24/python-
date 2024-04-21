# if statement

if(5>10):
    print("yes")
else:
    print('no')
    
#################################   
age1=int(input('enter age1'))
age2=int(input('enter age2'))
if(age1>age2):
    age3=age1+age2
    print('my age add',age3)
else:
    age3=age1-age2
    print('my age sub',age3)

#################################
    
email='vishnu@gmail.com'
pwd=123456
otp=987

#if else
uemail=str(input('enter email'))
upwd=int(input('enter the pwd'))
if(email==uemail and pwd==upwd):
    print('login success')
else:
    print('login failed')

#nested if else

uemail=str(input('enter email'))
upwd=int(input('enter the pwd'))
if(email==uemail):
    if(pwd==upwd):
        print('login success')
        uotp=int(input('enter otp'))
        if(otp==uotp):
                     print('transaction successful')
        else:
            print('transaction failed')
    else:
        print("login failed due to incorrect password")
else:
    print('login faileddue to incorrect email')

####################################################

#if elseif  (elif)

num1=30
num2=30
if(num1>num2):
    print(num1,'is greater')
elif(num1==num2):
    print('r equal')
else:
    print(num2,'is greater')
