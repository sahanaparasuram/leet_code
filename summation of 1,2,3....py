n=int(input("enter a number: "))
sum=0
tot=0
for i in range(1,n+1):
    tot=tot+i
    sum=sum+tot
    if i<n:
     print(tot,end='+')
    else:
        print(tot,end='=')
print(sum,' :)')
            
