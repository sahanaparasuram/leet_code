x=[4,5,6,7]
y=2.3
def f1(x, y):
     x+=['a','e','i','o','u']
     print("in function f1","x=",x," y=",y)
def f2():
     x=[9,22,45,34,67]
     y=3
     f1(x,y)
     print("in function f2","x=",x," y=",y)
#main
print(x,y)
f2()
print(x,y)

'''
[4,5,6,7] 2.3
in function f1 x= [9,22,45,34,67,'a','e','i','o','u'] y= 3
in function f2 x= [9,22,45,34,67,'a','e','i','o','u'] y= 3
[4,5,6,7] 2.3
'''
