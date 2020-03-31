L=eval(input("enter elements: "))
lenl=len(L)
for j in range(0,lenl-1):
        while j>=0 and L[j+1]<L[j]:
            L[j+1],L[j]=L[j],L[j+1]
            j=j-1
print(L)
