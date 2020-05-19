def fun1(a, b):
     y=4
     def f2(c, d):#8,20
         d=c+y+2#14
         return d
     a=a+2#8
     b*=2#20
     b=f2(a,b)#30
     print(a,b,y)#8,30,4
     return a,b#8,30
x=6
y=10
print(x,y)
x,y=fun1(x,y)
print(x,y)#8,14

'''
6 10
8 14 4
8 14

'''
