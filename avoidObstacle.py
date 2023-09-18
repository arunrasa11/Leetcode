def solution(p):
    x = set(list(range(2, max(p) + 2, 1)))
    xy = sorted(x - set(p))

    for i in xy:
        rem = min([j % i for j in p])
        if rem != 0:
            return i

    return max(p) + 1


p = list(range(1, 100, 19))

print(solution(p))