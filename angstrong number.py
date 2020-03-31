u=int(input("enter upper limit: "))
l=int(input("enter the lower limit: "))


sum=0
for i in range(l,u+1):
    leng=len(str(i))
    n=leng
    while leng>0:
      dig=i-((i//10)*10)
      i=(i-dig)/10
      fin=dig**n
      sum=sum+fin
      leng=leng-1
    if i==sum:
        print(i)
