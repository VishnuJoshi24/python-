# To check leap year
year=int(input('enter the year  '))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("is leap year")
else:
    print('is not leap year')


print()
print()

#######################################################################

n=int(input('enter the year  '))
if n%4==0:
    if n%100==0:
        if n%400==0:
            print("leap year")
        else:
            print("not leap year")
    else:
        print("leap year")
else:
    print('not leap year')