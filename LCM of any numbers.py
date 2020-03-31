L=eval(input("enter numbers(seperate numbers with commas): "))#1,5,2,4,3
l=len(L)
mul=1
max=L[0]
for i in L:
    for a in L:
        if i>max:
            max=i
for i in L:
    if i!=max:
        mul=i*mul
for i in range(max,max*mul+1):#5,120
    for a in L:
        if i%a==0:
            chk=1
        else:
            chk=0
            break
    if chk==1:
        LCM=i
        break
print("LCM of the numbers is: ",LCM)

        
    
    
