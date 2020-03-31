n=int(input("enter a number: "))
fact=1
x=n
while x>0:
    fact=x*fact
    x=x-1
print(n,'! = ',fact)
