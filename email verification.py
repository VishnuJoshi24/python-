#email verification using nested if 
email='vishnu@gmail.com'
pwd=123456
otp=987

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
    print('login failed due to incorrect email')
    
# ########################################################
