nums=eval(input('enter n: '))
target=int(input('enter  target: '))
cl1=(target-nums[0])
c1=nums[0]
for i in range(0,len(nums)):
    if (nums[i]-target)**2<(cl1)**2:
        print(i)
        cl1=nums[i]-target
        c1=nums[i]
        nums.pop(i)
        
cl2=(target-nums[0])
c2=nums[0]
for i in range(0,len(nums)):
    if (nums[i]-target)**2<(cl2)**2:
        cl2=nums[i]-target
        c2=nums[1]
        nums.pop(i)
        
cl3=(target-nums[0])
c3=nums[0]
for i in range(0,len(nums)):
    if (nums[i]-target)**2<(cl3)**2:
        cl3=nums[i]-target
        c3=nums[i]
        nums.pop(i)
        
print('the sum that is closest to the target is',c1+c2+c3,'(',c1,'+',c2,'+',c3,'=',c1+c2+c3,')')
            
