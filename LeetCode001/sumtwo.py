def twoSum(nums, target):
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if target-nums[i]==nums[j]:
                print(i,j) 
                j=j+1
            else:
                j=j+1
        i=i+1
nums=[2,7,11,15,1,8,3,6]
target=9
twoSum(nums,target)
            