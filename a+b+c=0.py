a=eval(input('enter an array: '))#[-1,0,-1,2,4]
l=[]

n=len(a)#5
for i in range(0,n):
    
    for j in range(i+1,n):
        
        for k in range(j+1,n):
            t=[]
            if a[i]+a[j]+a[k]==0:
                
                t+=[a[i],a[j],a[k]]
                
                
                
            if t!=[] and t not in l :
                l.append(t)
print(l)
for i in l:
    print(i)
   
    
