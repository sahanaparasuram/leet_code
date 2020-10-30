import math
nums = eval(input('enter an array of integers: '))
sum = 0
sums = []
target = int(input('enter target: '))
le=len(nums)
for i in range(0,le):
    for j in range(i+1,le):
        for k in range(j+1,le):
            sum=0
            sum+=(nums[i]+nums[j]+nums[k])
            sums+=[[nums[i],nums[j],nums[k]]]
            if sum == target:
               flag = target
fin=sums[0][0]+sums[0][1]+sums[0][2]
print(sums)
for i in sums:
    tot=0
    for j in i:
        tot+=j
    if math.fabs(target-fin)>math.fabs(target-tot):
        fin=tot
    print(fin,tot)

print('the value closest to the target is :',fin)
            
                  
