def prime(x):
    
    count=2
    for i in range(2,x):
        if x%i==0:
            count=count+1
            
    if count==2:
        print("this is a prime number:)")
    else:
        print("this is not a prime number")

n=int(input("enter a number: "))
prime(n)
        
