l=eval(input('enter an array: '))#[0,0,0,1,1,1,1,1,0]
a=[]
min=int(input('enter min value: '))
max= int(input('enter max value: '))
leng=len(l)#5
flag=0
if l[0]==0:
    a=[1]
    for i in range(1,leng):
        a.append(0)
        
else:
    flag = 0
i=0
while i<leng-1:#[0,1,1,1,1,1,0]
                          #[1,0,0,0,0,0,0]
    
    if a[i]==0:
        i+=1
        continue
    if l[i+1]==0:
        a[i+1]=1
        
                
    for j in range(min,max+1):
        if i+j<leng:
             if l[i+j]==0:
                  a[i+j]=1
    i+=1
        
print(a)    
print(flag) 
if a[leng-1]==1:
    flag=1
    
if flag==1:
    print('yayyyy!! this game can be won!! :)')
else:
    print('sorry!! you cannot win this!! :(')

    
