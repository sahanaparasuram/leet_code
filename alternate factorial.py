x= int(input("enter x: "))
fact=1
fact1=1
fact2=1
sum=0
for i in range(1,x+1):
    fact=((fact*i)*((-1)**(i+1)))
    if i<x:
        if i%2==0:
            print(fact,end='+')
        else:
            print(fact,end='')
    else:
        print(fact,end='=')
    
    sum=sum+fact
    if fact<0:
        fact=-fact
    else:
        fact=fact
print(sum)
         
