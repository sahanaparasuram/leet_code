a=input('enter a string: ')#sahana
a=list(a)
r=int(input('enter number of rows: '))#3
''' s n  
      aaa 
      h   '''

l=[]
flag=1
for i in range(0,r):
    g=[]
    g+=a[i]
    l.append(g)


i=r
while i < len(a):
    if flag==1:
        for j in range(r-2,0,-1):
            l[j].append(a[i])
            i+=1
            
    else:
        for j in range(0,r):
            if i<len(a):
               
                l[j].append(a[i])
                i+=1
                
            else:
                break
    flag*=(-1)
final=''
for i in l:
    for j in i:
        final+=j
print(' :) your final string is : ',final)
        
            
            
        
        
    
    
    
    
        
    
