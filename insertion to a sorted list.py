l=eval(input('enter a list: '))
n=int(input('number to be apended: '))

for i in range(0,len(l)):
    
    if l[i]>n:
        index = i
        print(index)break
    else:
        index=len(l)
    
        
l.append(0)

for i in range(len(l)-1,index,-1):
    if n==len(l-2):
        break
    l[i]=l[i-1]
    print(l[i-1])

l[index] = n
print(l)
    
    
    
        
    
