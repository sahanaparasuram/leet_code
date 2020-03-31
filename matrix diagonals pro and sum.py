l=eval(input('enter a 2D list: '))#
sum=0
pro=1
a=b=len(l)
z=0


for i in range(0,a):
    
    
        for j in range(0,a):
            if i==j or i+j==a-1:
                print(l[i][j],end=' ')
             
            else:
                print(' ',end=' ')
        print()
 
