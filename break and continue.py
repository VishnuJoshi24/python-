#Break statement
for i in range(1,101):
    if i==50:
        break
    print('roll no allowed',i)
print()

############################################
#continue statement
   
for i in range(1,101):
    if i==50 or i==25 or i==75:
        continue
    print('roll no allowed ',i)
print()
# #############################################

# swap 

a,b=10,20
a,b=b,a
print(a,b)
        