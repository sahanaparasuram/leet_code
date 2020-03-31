
#version 1

l = eval(input('enter an array :) '))#[0,1,1,1,1,1,1,0]
min=int(input('enter a min value: '))
max=int(input('enter a max value: '))
shoe=True
i=0
while shoe and i<len(l)-1:
    
    if l[0]==1 or l[len(l)-1]==1:
        print('sorry! you can\'t win :(')
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
                print('sorry! you can\'t win :(')
                shoe=False
                break
        else: 
            shoe = False
            print('sorry! you can\'t win :(')
            break
            
           
                
               
               
if i == len(l)-1:
    print('yayy!!you can win this game! :)')
    
        

    
