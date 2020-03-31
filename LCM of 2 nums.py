x=int(input("enter a number: "))
n=int(input(" enter another number: "))
if x>n:
    big=x
    small=n
else:
    big=n
    small=x
for i in range(big,big*small+1):
    if i%small==0 and i%big==0:
        print(i)
        break
    
