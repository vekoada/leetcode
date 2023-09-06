def twoSum(nums, target):
    seen = {}
    for i in range(len(nums)):
        if (target - nums[i]) in seen:
            return [seen[target - nums[i]], i]
        else:
            seen[nums[i]] = i


def twoSum2(nums, target):
    seen = {}
    for i, el in enumerate(nums):
        req = target - el
        if req in seen:
            return [seen[req], i]
        seen[el] = i

print(twoSum2(nums=[2, 7, 11, 15], target=9))
