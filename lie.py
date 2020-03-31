n=int(input("enter a number: "))
chk=0
for i in range(2,(n//2)+1):
    if n%i==0:
        chk=1
        break
if chk==0:
    print("this number is a prime number")
else:
    print("this number is a composite number")
