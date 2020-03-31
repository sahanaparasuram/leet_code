d=int(input("enter day(eg: if the date is 10/3/24, enter 10): "))
m=int(input("enter month number: "))
y=int(input("enter year: "))
do=0
if m==1:
    if y%400==0 or(y%4==0 and y%100!=0):
        do=4
    else:
        d0=3
elif m==2:
    if y%400==0 or(y%4==0 and y%100!=0):
        do=28
    else:
        d0=29
elif m%2==0 and do!=2:
    do=m
elif m==3:
    do=14
elif m==5:
    d0=9
elif m==7:
    do=11
elif m==9:
    do=5
elif m==11:
    do=7
dom=y//100
if dom%4==0:
    a=2
elif dom%4==1:
    a=0
elif dom%4==2:
    a=5
elif dom%4==3:
    a=3
b=(y-((y//100)*100))//12
c=(y-((y//100)*100))%12
e=c//4
sum=a+b+c+e
if sum>=7:
    sum=sum-7
    if sum<7:
        sum=sum
        
    else:
        sum=sum-7
        
        if sum<7:
            sum=sum
            
        else:
            sum=sum-7
            
            if sum<7:
                sum=sum
                
            else:
                sum=sum-7
                sum=sum
                
if sum==1:
    day='mon'
elif sum==2:
    day='tues'
elif sum==3:
    day='wed'
elif sum==4:
    day='thurs'
elif sum==5:
    day='fri'
elif sum==6:
    day='sat'
elif sum==0:
    day='sun'
print("the doomsday of the year is: :",day)
print("the doomsday of the month is: ",do)

if d<do:#problem is here
    
    if do<7:
        x=do-d
        sum=sum-x
        
    elif do==7:
        x=do-d
        sum=sum-x
        
    elif do>7:
        do=do-7
        
        if do>=7:
            
            do=do-7
            
        else:
            
            if do>=7:
                do=do-7
                
        x=do-d
        sum=sum-x
elif d==do:
    sum=sum
    
elif d>do:
    #correct till here
    if (d-do)<7:
        do=do
        
    elif (d-do)==7:
        print(do)
        do=do+7
       
    else:
        
        do=do+7
        
        if (d-do)<7:
            do=do
            
        else:
            do=do+7
            
    x=d-do
    sum=sum+x
    
    if sum>6:
        sum=sum-7
        #sum

if sum==1:
    day='mon'
elif sum==2:
    day='tues'
elif sum==3:
    day='wed'
elif sum==4:
    day='thurs'
elif sum==5:
    day='fri'
elif sum==6:
    day='sat'
elif sum==0:
    day='sun'
print("the day of this date is: ",day)




    
                    
        



    
