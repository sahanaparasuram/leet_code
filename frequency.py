L=eval(input("enter a list: "))
l=len(L)
count=0
for i in range(0,l+1):
    for k in range(0,l+1):
        if L[i]==L[k]:
            count=count+1
            L.pop(i)
            l=l-1
            if k==l-1:
                break
             
        else:
            continue
    if i==l-1:
        break
    print("the number",i,"was found",count,"times")
            
