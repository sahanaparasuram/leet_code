n=int(input('enter a number: ' ))#1234
temp=n
a=len(str(n))
num=0
for i in range(0,a):
    if n//10!=0:
        dig = n-(n//10)
    else:
        dig=n
    print('num',num)
    print('n',n)
    n=(n-dig)/10
    print('dig',dig)
    num+=dig
    if i!=a-1:
        num*=10
    print('num',num)
if num==temp:
    print('yesss!!!')
else:
    print('no :(')
    
    

            
