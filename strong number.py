a=int(input("enter a number: "))#145
dig=0
new=0
temp=a
sum=0
lena=len(str(a))
for i in range(0,lena):
    fact=1
    dig=a%10#5
    
    for j in range(1,dig+1):
        fact=fact*j
    sum=sum+fact
    a=a//10
if sum==temp:
    print("congratulations! it is a strong number!")
else:
    print("it isnt a strong number :(")
    
    
    
