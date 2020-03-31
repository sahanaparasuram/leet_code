a=input('enter a string: ')#pwwkew
l=[]

max=[]
for i in range(0,len(a)):
    s=a[0] 
    for j in range(i+1,len(a)):
        
        if a[i]!=a[j] and a[j] not in s:
            s+=a[j]
        else:
            break
    
    l.append(len(s))
    a= a[len(s)-1:len(a)]
    print(a)

print(l)
max=l[0]
for i in l:
    if i>=max:
        max=i
print(max)
