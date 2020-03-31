a=eval(input('enter list A: '))
b=eval(input('enter list B: '))
f=[]
for i in range(0,len(a)):#r1
    r=[]
    for j in range(0,len(b[0])):#c2
        sum=0
        for k in range(0,len(a[0])):#c1
            sum+=a[i][k]*b[k][j]
        r.append(sum)
    print(sum)
    f.append(r)
print(f)
