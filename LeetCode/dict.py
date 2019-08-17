def twoSum(nums, target):
        tmp_dict={}
        for index,val in enumerate(nums):
            diff=target-val
            if diff in tmp_dict:
                return [tmp_dict[diff],index]
            else:
                tmp_dict[val]=index
nums=[2,7,11,15,1,8,3,6]
target=9
print(twoSum(nums,target))               