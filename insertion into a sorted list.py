l=eval(input('enter a list:  '))
num = int(input('enter a number: '))
if len(l)>0 and l[-1]>num:
    for  i in range(0,len(l)):
        if l[i]>num:
            pos=i
            break
        
        
            
    l.append(0)
    
        
    for i in range(len(l)-1,pos,-1):
        l[i]=l[i-1]

    l[pos]=num
    
else:
    l.append(num)

    
    

        
