m=[[1,2,3],[4,5,6],[7,8,9]]
r=len(m)
c=len(m[0])
m1=[]
m2=[]

# printing matrix

for i in m:
    for j in range(0,len(m[0])):
        print(i[j],end=' ')
    print()
print()

# printing transpose of the matrix

for i in range(0,r):
    r1=[]
    for j in range(0,c):
        r1+=[m[j][i]]
    m1.append(r1)
for i in m1:
    for j in range(0,len(m1[0])):
        print(i[j],end=' ')
    print()
    
print()

# printing 90 degree rotated matrix

for i in range(0,len(m[0])):
    r2 = []
    for j in range (len(m)-1,-1,-1):
        r2+=[m[j][i]]
    m2.append(r2)

for i in range(0,len(m2[0])):
    for j in range(0,len(m2)):
        print(m2[i][j],end = ' ')
    print()
        
