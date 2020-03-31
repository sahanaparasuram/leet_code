n=input('enter a string of integers: ')
a=0
for i in n:
    a+=ord(i)-48
    if i!=n[len(n)-1]:
        a*=10
print(n)
print(a)
print('a:',type(a),'n:',type(n))
