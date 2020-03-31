sum=1
fact=1
n=int(input("enter a number: "))
for i in range(3,n+1):
    fact=fact*i*(i-1)
    sum=sum+fact
print(sum)
    
