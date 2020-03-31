x=int(input("enter a number: "))
y=int(input("enter another number: "))
sumx=0
sumy=0
for i in range(1,(x//2)+1):
    if x%i==0:
        
        sumx=sumx+i
        
for k in range(1,(y//2)+1):
    if y%k==0:
        
        sumy=sumy+k
        
if sumy==x and sumx==y:
    print('the two numbers are amicable pairs')
else:
    print("the two numbers are not amicable pairs")
    
