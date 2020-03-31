L=[3,1,5,2,6,3,7,4,5,5,9,8,0,6]
print('original list:\n\n',L)
l=len(L)

# bubble sort - my method

for i in range(0,l):
    for j in range(1,l-i):
        if L[j-1]>L[j]:
            L[j-1],L[j]=L[j],L[j-1]

print()
print('sorted lists: ')
print()
print(L)
    
# insertion sort

L=[3,1,5,2,6,3,7,4,5,5,9,8,0,6]

for i in range(1,l):
    num=L[i]
    j=i-1
    while j>=0 and num<L[j]:
        L[j+1] = L[j]
        j=j-1
    else:
        L[j+1] = num
print (L)

# bubble sort - school method

L=[3,1,5,2,6,3,7,4,5,5,9,8,0,6]

l=len(L)
for i in range(0,l):
    for j in range(0,l-i-1):
        if L[j+1]<L[j]:
            L[j+1],L[j]=L[j],L[j+1]
print(L)


