#loop

#for     use n=(n+1)
for i in range(1,6):
    print('$')
    print()
    
for i in range(1,6):
    print('*',end=' ')  #end is used to print in same line
    
###  pattren program  ###
    
    
for i in range(1,6):
    for j in range(1,i+1):
        print('*',end=' ')
    print()
    
print()    
#################################

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=' ')
    print()

print()

#################################
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=' ')
    print()
print()

################################
    
for i in range(65,91):
    for j in range(65,i+1):
        print(chr(j),end=' ')
    print()
print()

################################
for i in range(1,11):
    print((i/10),end=' ')
print()

################################
