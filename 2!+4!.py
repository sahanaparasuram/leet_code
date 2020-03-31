n=int(input("enter a number: "))
fact=1
sum=0
for i in range(2,n+1,2):
    fact=fact*i*(i-1)
    if i<n:
        print(fact,end='+')
    else:
        print(fact,end='=')
    sum=sum+fact
print(sum)
