
#version 2

l = eval(input('enter an array :) '))#[0,0,1,0,1,0,1,1,0]
min=int(input('enter min value: '))
max=int(input('enter max value: '))
shoe=True
i=0
flag=0
if len(l)==1 and l[0]==1:
    flag = 0
while shoe and i<len(l)-1:
    
    if l[0]==1 or l[len(l)-1]==1:
        flag=0
        break
    
        
    else:       
        for j in range(max,min-1,-1):
            if (i+j)<(len(l)):
                if l[i+j]==0:
                    i+=j
                    break
                if j == min:
                    if l[i+1]==0:
                        i+=1
                    
                
                    
            else:
                continue
        else: 
            shoe = False
            flag=0
            break

if i == len(l)-1 and l[i]==0:
    flag=1
if flag ==0:
    
    shoe=True
    i=0
    while shoe and i<len(l)-1:
    
        if l[0]==1 or l[len(l)-1]==1:
            flag=0
            break
        if l[i+1]==0:
            i+=1
            shoe = True
        
        else:       
            for j in range(min,max+1):
                if (i+j)<=(len(l)-1):
                    if l[i+j]==0:
                        i+=j
                        shoe=True
                
                        break
                else:
                    flag=0
                    shoe=False
                    break
            else: 
                shoe = False
                flag=0
                break
            
           
                
           
                
               
               
if i == len(l)-1 and l[i]==0:
    flag=1


if flag == 0:
    print('sorry you can\'t win this game! :(')
else:
    print('yayy!! you can win this game :)')
        

    
