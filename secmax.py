L=eval(input("enter elements(please enter values within [],each value separated by a comma) : "))
l=len(L)
max=L[0]
secmax=L[0]
for i in range(0,l):
    num=L[i]
    if num>=max:
        max=num
    else:
        secmax=num
for i in range(0,l):
    if L[i]>=secmax and L[i]<max:
        secmax=L[i]
print("the secoond max value is: ",secmax)
