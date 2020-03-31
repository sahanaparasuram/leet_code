
i=int(input("enter a number: "))
temp=i
sum=0
leng=len(str(i))
n=leng
while leng>0:
    
      dig=i-((i//10)*10)
      i=(i-dig)/10
      fin=dig**n
      sum=sum+fin
      leng=leng-1
if sum==temp:
    print("this is an angstrong number")
else:
    print("no")
