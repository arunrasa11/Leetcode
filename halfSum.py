def equivalent_index(nums):

    # half_sum = sum(nums) / 2
    # idx = int(len(nums) / 2)
    # left_list = nums[:idx]
    # right_list = nums[idx:]
    #
    # if sum(left_list) == half_sum:
    #     return idx
    # elif sum(left_list) < half_sum:
    #     while sum(left_list) < half_sum:
    #         idx = idx + 1
    #         left_list = nums[:idx]
    #         if sum(left_list) == half_sum:
    #             return idx - 1
    # else:
    #     while sum(right_list) < half_sum:
    #         idx = idx - 1
    #         right_list = nums[idx:]
    #         if sum(right_list) == half_sum:
    #             return idx - 1
    # return -1

    half_sum = sum(nums) / 2
    for i in range(len(nums)):
        if sum(nums[:i]) == half_sum:
            return i-1
        elif sum(nums[:i]) > half_sum:
            break
    return -1



nums = [1, 7, 3, 5, 6]
print(equivalent_index(nums))