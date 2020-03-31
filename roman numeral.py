# I V X L C D M
n=input('enter a roman numeral: ')#IV
d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
num=0
i=0
while i<len(n):
    if i!=len(n)-1 and d[n[i]]<d[n[i+1]]:
        num+=d[n[i+1]]-d[n[i]]
        i+=2
        
    else:
        num+=d[n[i]]
        i+=1
        
print(num)
