n=int(input("enter a number: "))
a=1
temp=n
r=0
for i in range(0,n):
    for j in range(0,a):
        temp-=1
    if temp<0:
        break
    r+=1
    a+=1
print ('rows : ',r)
