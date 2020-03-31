l=eval(input('enter an array: '))
n=int(input('enter a target: '))
a=[]
flag=0
for i in range(0,len(l)):
    for j in range(1,len(l)):
         if l[i]+l[j]==n:
            flag=1
            break
    if flag == 1:
         break
a.append(i)
a.append(j)
print(a)
