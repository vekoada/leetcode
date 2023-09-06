def twoSum(nums, target):
    for i in range(len(nums)):
        if (target - nums[i]) in nums and nums.index(target - nums[i]) != i:
            return [i, nums.index(target - nums[i])]
    return []

print(twoSum(nums=[2, 7, 11, 15], target=9))