
a = 5
def scopefun():
     a=10
     print ("a funcscope before loop",a)
     for i in range (1,3):
         a=100
         print("a in for loop:",a)
         a+=1
     print("a in function scope after for loop",a)
#main
print ("a in main before function call",a)
scopefun()
print("a in main after function call",a)

'''
a in main before function call 5
a funcscope before loop 10
a in for loop:100
a in for loop:100
a in function scope after for loop 101
a in main after function call 5
'''
