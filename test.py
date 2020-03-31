def cir(x,y,z):
    
        x+=y+z
        y*=z*x
        z-=x-y
        
        print('x',x,'y',y,'z',z)
        if z>y:
            return y
        else:
            return z
a=4
b=2
c=3
print('find',cir(c,b,a))
print('a',a,'b',b,'c',c)
b=cir(c,b,a)
print('a',a,'b',b,'c',c)
c=cir(c,z=3,y=2)
print('a',a,'b',b,'c',c)
