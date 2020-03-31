u=int(input("enter the upper limit: "))
l=int(input("enter the lower limit: "))
if l==1:
    l=l+1
print("the prime numbers in the range are: ",end='')
for i in range(l,u+1):
    chk=0
    for k in range(2,i):
        if i%k==0:
            chk=1
            break
    if chk==0:
        print(i)
