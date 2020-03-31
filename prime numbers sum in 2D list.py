sum=2
m=[[1,2,3],[4,5,6],[7,8,9]]
r=len(m)
c=len(m[0])
for i in range(0,r):
    for j in range(0,c):
        
        n=m[i][j]
        if n==1 or n==2:
               continue
        chk=0
        for k in range(2,n):
            if n%k==0:
                chk=1
                break
        if chk==0:
            sum+=n
print(sum)
        
