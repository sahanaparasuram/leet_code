p=3
def funout(n):#4
      p=8
      def funin(r):#1,3
          global p #modifying p to nonlocal
          p=r*10# 10,30
          print(p,r)#10,1,30,3

      for i in range(1,n,2):
          funin(i)
      print(p)
funout(4)
print(p)

'''
10 1
30 3
8
30

'''
