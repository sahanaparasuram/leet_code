x=int(input("enter x: "))
n=int(input("enter n: "))
sum=0
for i in range(2,n+1,2):
    if i%4==0:
         fin=((x**i)/(i+1))
    else:
        fin=((x**i)/(i+1))*(-1)
    if i<n:
        if i%4==0:
            print(fin,end='')
        else:
            print(fin,end='+')

    else:
        print(fin,end='=')
    sum=sum+fin
print(sum)
    
