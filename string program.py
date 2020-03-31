count=0
count1=0
L=[]
s=input("enter the string: ")
n=int(input("enter number: "))
for i in s:
    if i==' ':
        count=count+1
count=count+1
for i in range(0,count):
    str=''
    count1=0
    for j in s:
        if j!=' ':
            count1+=1
            str=str+j
        else:
            break
    if count1>n:
        L=L+[str]
    s=s[count1+1::]
print(L)
            
