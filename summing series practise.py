x=int(input("enter x: "))
n=int(input("enter n: "))
sum=0
for i in range(1,n+1):
    fin=x**i
    if i<n:
     print(x**i,end=' + ')
    else:
     print(x**i,end=' = ')
    sum=sum+fin
print(sum)
    
