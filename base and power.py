def power(b,p):
    if b==0:
        return 1

    if p==1: 

        return(b) 

    else: 

        return(b*power(b,p-1)) 

b= int(input('enter base: ')) 

p = int(input('enter power: ')) 

print('result:', power(b,p)) 

  
