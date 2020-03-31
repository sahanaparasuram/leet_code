a=eval(input("enter elements: "))#12345
b=eval(input("enter elements: "))#67890
chk=1

for i in range(0,len(a)):#0,5
    for j in range(0,len(b)):#0,5
        if a[i]==b[j]:
            chk=0
            break
if chk==0:
    print("intersected")
else:
    print("seperated")
            
