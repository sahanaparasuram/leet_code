x=int(input("enter number of rows: "))
if x%2==0:
    b=(x//2)+1
    c=(x-b)+1
else:
    b=(x//2)+2
    c=(x-b)+1

for i in range(1,b):
    for a in range(1,i+1):
        print('*',end='')
    print()
    

for i in range(c,0,-1):
    for a in range(0,i):
        print("*",end='')
    print()
