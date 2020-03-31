n=int(input("enter n: "))
fact=1
sum=1
print("1",end='+')
for i in range(3,n+1,2):
    fact=fact*i*(i-1)
   
    sum=fact+sum
    if i<n:
        print(fact,end='+')
    else:
        print(fact,end='=')
print(sum)
