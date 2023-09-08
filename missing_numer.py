def missing_number(nums):
    # for i in range(len(nums)):
    #     if i not in nums:
    #         return i
    #         break

    n = len(nums)
    sum1 = (n*(n+1))/2
    list_sum = sum(nums)
    return sum1 - list_sum

nums = [0,1,2,4,5]
print(missing_number(nums))