rows=int(input("enter rows: "))
k=1
for i in range(3,-1,-1):
    for j in range(i,0,-1):
        print(' ',end='')
    for a in range(0,2*k-1,):
        print("*",end='')
    k=k+1
    print()
