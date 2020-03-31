n = int(input('enter the number of levels: '))

levels_0=[]
levels_1=[]

N_moves=[1,3,4]

# the moves can be 1,3,4
for i in range(0,n+1):
    a=i-1
    b=i-3
    c=i-4
    
    if i==0 or i==2:
        flag = 0
        levels_0.append(i)
        continue
        
    elif i==1 or i==3 or i==4:
        flag=1
        levels_1.append(i)
        continue

    if (a in levels_0) or (b in levels_0) or (c in levels_0):
        flag = 1
        levels_1.append(i)

    if (a in levels_1) and (b in levels_1) and (c in levels_1):
        flag= 0
        levels_0.append(i)

if (n in levels_1):
    while n>0:
        print('yayy!! you are on a winning level!!\nlets see if you are smart enought to play the game!')
        ym=int(input('enter your move: '))
        n = n-ym
        if n==0:
            print('yayyy!! you won well done')
            
            break
        if n in levels_0:
            
            nm = N_moves[random.randint(0,2)]
            print('the NIM has moved you to level',n-nm)
        else:
            if n-1==

    
    
    
    
            
    
else:
    print('oops! you are going to loose to the NIM!')


