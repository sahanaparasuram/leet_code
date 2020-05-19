q =10
def scp_fn( x,y ,z):
     p = x

     global q
     q= y + z
     print(p,q,y,z)
#main
p = 5
r = 7
print(p,q,r)
scp_fn(p,q,r)
print(p,q,r)

'''
5 10 7
5 17 10 7
5 17 7
'''
