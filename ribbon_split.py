def solution(a, k):
    # sum1 = sum(a)
    # num = int(sum1 / k)

    # while num >= 1:
    #     count = 0
    #     for val in a:
    #         count += int(val / num)
    #         if count >= k:
    #             return num
    #     num = num-1

    left, right = 0, max(a)
    while left < right:
        mid = (left + right + 1) >> 1    # bit wise operator >>1 equals to //2 but faster
        cnt = sum(x // mid for x in a)
        if cnt >= k:
            left = mid
        else:
            right = mid - 1
    return left



a= [5, 2, 7, 4, 9]
k= 5
print(solution(a,k))
