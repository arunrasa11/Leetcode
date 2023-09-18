def solution(l):
    n = len(l) - 1
    while n > 0:
        if l[n] <= l[n - 1]:
            n -= 1
        else:
            break
    n = n - 1

    if n == -1:
        l[:] = l[::-1]
    else:
        i = len(l) - 1
        while i >= n:
            if l[n] >= l[i]:
                i -= 1
            else:
                break
        x = l[n]
        l[n] = l[i]
        l[i] = x
        l[n + 1:] = l[:n:-1]

    return l


nums = [1, 5, 1]
nums = [5, 1, 1]
nums = [2, 3, 8, 5, 4, 1, 0]
print(solution(nums))

