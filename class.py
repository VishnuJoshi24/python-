class mango:
    def __init__(self):
        print('this is what?=constructure') #constructure
    def balaji(self):
        print('function without parameter')
    def fun(self, a,b):
        print(a+b,'function with parameter')
    def neon(self,a):
        print('check neon or not')
       
        '''only 0,1,9 are neon num
            0*0==0 neon
            1*1==1 neon
            9*9=81=8+1==9 neon'''
man=mango()
man.balaji()
man.fun(10,20.5)
man.neon(7)