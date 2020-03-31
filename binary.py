a=eval(input('enter an array: '))
n=int(input('enter a number to be searched: '))

i=0
flag=0
while True:
    x=len(a)-1
    if x<0:
        break

    if a[(x//2)]==n:
        flag=1
        break
        
    elif n>a[x//2]:
        a=a[(x//2)+1:x+1]
        
    elif n<a[x//2]:
        a=a[0:(x//2)]
    
    
    print(a)
    print(i)
    
if flag==1:
    print('yess')
else:
    print('sorry your element is not found :(')
            
