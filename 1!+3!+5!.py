n=int(input("enter n: "))
fact=1
sum=1
print(1,'!',end=' + ')
for i in range(3,n+1,2):
    fact=fact*i*(i-1)
    if i<n-1:
        print(i,'!',end=' + ')
    else:
        print(i,'!',end=' = ')
    sum=sum+fact
print(sum)
    
