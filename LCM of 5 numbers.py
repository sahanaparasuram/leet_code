print("enter the numbers:")
a=int(input(""))
b=int(input(""))
c=int(input(""))
d=int(input(""))
e=int(input(""))
if a>b and a>c and a>d and a>e:
    big=a
    rest=b*c*d*e
elif b>a and b>c and b>d and b>e:
    big=b
    rest=a*c*d*e
elif c>a and c>b and c>d and c>e:
    big=c
    rest=a*b*d*e
elif d>b and d>c and d>a and d>e:
    big=d
    rest=a*b*c*e
else:
    big=e
    rest=a*b*c*d
for i in range(big,big*rest+1):
    if i%a==0 and i%b==0 and i%c==0 and i%d==0 and i%e==0:
        lcm=i
        break
print("LCM = ",i)
