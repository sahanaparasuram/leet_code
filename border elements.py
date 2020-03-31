f=[]
r=int (input('enter the number of rows: '))#[[1,2,3],[4,5,6],[7,8,9]]
c=int (input('enter the number of columns: '))
for i in range(0,r):
    ro=[]
    print('row',i+1,' elements:')
    for j in range(0,c):
        
        a=int(input('enter element:'))
        ro.append(a)
    f.append(ro)
print(f)
        
'''listen bro f is the final matrix ok
c is columns and r is rows
these are the shift right and left programs'''
for i in range(0,r):
    for j in range(0,c):
        print(f[i][j],end=' ')
    print()
print()
''' 1 2 3  7 4 1  3 6 9
    4 5 6  8 5 2  2 5 8
    7 8 9  9 6 3  1 4 7 '''
for i in range(0,c):
    for j in range(r-1,-1,-1):
        print(f[j][i],end=' ')
    print()

print()
for i in range(c-1,-1,-1):
    for j in range(0,r):
        print(f[j][i],end=' ')
    print()
    
