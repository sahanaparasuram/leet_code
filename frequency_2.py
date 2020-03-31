a=eval(input("enter elements: "))#1112231
count=0
j=0
i=0
lena=len(a)
while i<=lena:
    count=0
    j=0
    while j<=lena:
        if a[i]==a[j]:
            count+=1
            a.pop(j)
            lena=lena-1
    
    print(a[i], "was found" , count,"times")
    
