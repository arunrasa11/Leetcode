def twoSum(nums, target):

    # for idx, num in enumerate(nums):
    #     x = target-num
    #     if x in nums[idx+1:]:
    #         nums.pop(idx)
    #         return idx, nums.index(x)+1

    map = {}
    for idx, num in enumerate(nums):
        x = target - num
        if x in map:
            return map[x], idx
        else:
            map[num] = idx

    return []

nums = [3,2,4]
#nums = [3,3]
target = 6
print(twoSum(nums,target))