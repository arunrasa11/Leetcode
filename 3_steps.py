from functools import cache
from timeit import repeat
@cache
def steps_to(stair):

    if stair == 1:
        return 1
    elif stair == 2:
        return 2
    elif stair == 3:
        return 4
    else:
        return (
            steps_to(stair - 3)
            + steps_to(stair - 2)
            + steps_to(stair - 1)
        )


setup_code = "from __main__ import steps_to"
stmt = "steps_to(30)"
times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)
print(f"Minimum execution time: {min(times)}")

print(steps_to(30))

#53798080
#Minimum execution time: 3.3454087090067333


# manual caching

# def steps_to(stair):
#     cache = {}
#     return steps_to_cached(stair, cache)
#
# def steps_to_cached(stair, cache):
#
#     if stair == 1:
#         cache[stair] = 1
#         return cache[stair]
#     elif stair == 2:
#         cache[stair] = 2
#         return cache[stair]
#     elif stair == 3:
#         cache[stair] = 4
#         return cache[stair]
#     else:
#         if stair not in cache:
#             cache[stair] = steps_to_cached(stair-3, cache) + \
#                            steps_to_cached(stair-2, cache) + \
#                            steps_to_cached(stair-1, cache)
#         return cache[stair]
