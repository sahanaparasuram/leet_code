n=int(input('enter an integer: '))#476
temp=n
c=0
a=''
while n>0:
    n=n//10
    c+=1

n=temp
for i in range(c,0,-1):
    dig=n//(10**(i-1))
    a+=chr(dig+48)
    n=n-(dig*(10**(i-1)))
    
print('a:',a,type(a))
print('n:',temp,type(n))

