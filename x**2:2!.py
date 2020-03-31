x=int(input("enter a number: "))
n=int(input("enter n: "))
fact=1
sum=0
for i in range(2,n+1,2):
    fact=fact*i*(i-1)
    fin=(x**i)/fact
    if i<n:
        print(fin,end='+')
    else:
        print(fin,end='=')
    sum=sum+fin
print(sum)
