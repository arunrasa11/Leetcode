
def solution(nums):

    cach = {}

    for x in nums:
        n = len(str(x))
        if n in cach:
            cach[n].append(x)
        else:
            cach[n] = list()
            cach[n].append(x)
    print(cach)

    cach2 = {x:list() for x in range(10)}
    for x in nums:
        n = set(list(str(x)))
        for i in n:
            cach2[int(i)].append(x)
    print(cach2)



nums = [1,2,1,340,265,25,1,41]

print(solution(nums))