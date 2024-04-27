#function without parameters
def balaji():
    return'this is my bank balance'

test_dict={"fname":balaji,"age":50,"address":"salem"}
print('the original dictionary is :'+str(test_dict))
res=test_dict['fname']()

#function with parameters
def balaji(a,b):
    print('this is my bank balance=',a+b)

test_dict={"fname":balaji,"age":50,"address":"salem"}
print('the original dictionary is :'+str(test_dict))
res=test_dict['fname'](10,20)


for i in range(1,101):
    if i==50:
        break
    print('roll no ',i)
        