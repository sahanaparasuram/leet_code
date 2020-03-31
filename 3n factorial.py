n=int(input("enter n: "))
fact=1
sum=0
for i in range(3,(3*n)+1,3):
    fact=fact*i*(i-1)*(i-2)
    if i<(3*n):
        print(fact,end='+')
    else:
        print(fact,end='=')
    sum=sum+fact
print(sum)
