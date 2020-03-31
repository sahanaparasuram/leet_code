n=int(input('enter a number'))
temp=n
sum = 0
for i in range(0,len(str(temp))):
    dig = n-((n//10)*10)
    digpow = dig**(len(str(temp)))
    sum += digpow
    n = (n//10)
if sum == temp:
    print('yessss!!! go sleep ')
else:
    print('ok maybe a while longer...')
