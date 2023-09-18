def solution(a, b):

    # if len(a) != len(b):
    #     return False
    #
    # dict1 = {}
    #
    # for idx, x in enumerate(a):
    #     if x in dict1:
    #         set1 = dict1[x]
    #         set1.add(idx)
    #         dict1[x] = set1
    #     else:
    #         set1 = set()
    #         set1.add(idx)
    #         dict1[x] = set1
    #
    # swap = 0
    # for idx, y in enumerate(b):
    #     if y in dict1:
    #         if idx in dict1[y]:
    #             continue
    #         else:
    #             swap += 1
    #         if swap >= 3:
    #             return False
    #     else:
    #         return False
    #
    # return True

    from collections import Counter as C
    print(C(a))

    return sorted(a) == sorted(b) and sum([x != y for x, y in zip(a, b)]) <= 2

a= [1, 2, 2]
b= [2, 1, 1]
a=[1,1,1,2,1,1,1,1,1,1,1,1]
b=[1,1,1,1,1,1,1,1,1,1,1,2]
print(solution(a,b))