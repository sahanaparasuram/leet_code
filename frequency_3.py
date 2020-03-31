A=[1,2,3,4,1,2,3,1,2,1]
temp=A

while len(temp)>0:
    count=0
    a=temp[0]
    while a in temp:
        count+=1
        temp.remove(a)
    print(a,'occurs',count,'times')
