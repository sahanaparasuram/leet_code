l=eval(input('enter a 2D array: '))
#[[1,5],[3,4],[6,9],[7,2]]
max=0
cos=[]
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if l[j][1]>l[i][1]:
            small=l[i][1]
        else:
            small=l[j][1]

        area=(l[j][0]-l[i][0])*small
        if area>=max:
            max=area
            cos=[i+1,j+1]
        if  j!=len(l)-1 and l[j][1]>l[j+1][1] and l[j][1]>l[i][1] :
             break
print(max)
print(cos)
