l = eval(input('enter a list: '))
if len(l) == 1:
    print (l[0])
else:
     if l[0]>=l[1]:
        print(l[0],end=' ')
     if l[len(l)-1]>=l[len(l)-2]:
        print(l[len(l)-1],end=' ')
     for i in range(1,len(l)-1):   
        if l[i]>=l[i-1] and l[i]>=l[i+1]:
            print(l[i],end=' ' )
            break
        
    
n = int(input('enter n: '))
