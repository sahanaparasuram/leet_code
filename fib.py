


    
 

a=0 

b=1 

i=2 

x=int(input('enter no. of terms: ')) 

  

print(b,end=' ') 

def fib(n): 

    global a 

    global b 

     

    f= a+b 

    a=b 

    b=f 

    print(f,end=' ') 

    global i 

    if i < n: 

        i+=1 

        fib(n) 

         

  

fib(x) 
