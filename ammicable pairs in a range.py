l=219
u=2000

sum=0
sumsum=0

for i in range(l,u+1):
    
    for j in range(1,i):
        if i%j==0:
            sum=sum+j
    if sum>=l and sum<=u:
        for k in range(1,sum):
            if sum%k==0:
                sumsum+=k
    if sumsum==i:
         print(i,sum)
            
        
