n=int(input("enter n: "))
a=0
b=1
print(a,b,end=' ')
for i in range(3,n+1):
    fib=a+b
    a=b
    b=fib
    
    print(fib,end=' ' )
