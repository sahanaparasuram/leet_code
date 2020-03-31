a=eval(input("enter the elements in ascending order: "))#[1,2,7,8,9]
b=eval(input("enter the elements in ascending order: "))#[3,4,5,6]
if a[-1]>b[-1]:
    c=b+a
else:
    c=a+b

print(c)
lena=len(a)
lenb=len(b)
if lena<lenb:
    val=lena
else:
    val=lenb
r=0
for i in range(0,val):
    if a[i]<b[i]:
        c[r]=a[i]
        c[r+1]=b[i]
        r=r+2
print(c)
