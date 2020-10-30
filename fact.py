
def factorial(n):
    fact=1
    for i in range(2,n+1):
        if i==1:
           break
        fact=fact*i
        
    print('the factorial of',n,'is',fact)


x=int(input("enter a number: "))
factorial(x)
