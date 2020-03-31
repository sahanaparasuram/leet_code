b=eval(input("enter elements: "))
if len(b)%2==0:
    lenb=len(b)
else:
    lenb=len(b)-1
for i in range(0,lenb,2):
    b[i],b[i+1]=b[i+1],b[i]
print(b)
