file = open('letter.txt','w')
def function(x):
    for i in range(0,x):
        str=input('enter string')
        str = str+'\n'
        file.write(str)
    file.close()

n = int(input('enter no. of lines'))
function(n)

file1 = open('letter.txt','r')
file2=open('line.txt','w')
def function2():
    for j in range(0,n):
        s= file1.readlines()
        p=s+'\n'
        if s[0] in 'aeiouAEIOU':
            file2.write(p)

a = file1.read()
print(a)
file1.close
file2.close

file3 = open('line.txt','a')
m = int(input('enter no. of lines to be appened'))
file3.write('\n')
def function3(q):
    for i in range(0,q):
        str1=input('enter string: ')
        str1=str1+'\n'
        file3.write(str1)

function3(m)
file3.close
