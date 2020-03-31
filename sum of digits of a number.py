''' first input some number and somehow find the sum of the digits'''
n=int(input("enter a number: "))
num=len(str(n))
dig=0
x=n
sum=0
while num>0:
    dig=x-((x//10)*(10))
    sum=sum+dig
    x=((x//10))
    num=num-1
    
print("sum : ",sum)
