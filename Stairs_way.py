def count_ways(steps: int) -> int:

    if steps <= 2:
        return steps
    else:
        # return count_ways(steps-1) + count_ways(steps-2)
        cache = [0, 1, 2]
        for x in range(3, steps + 1):
            cache = recur(cache)
        return cache[-1]


def recur(cache):
    return cache[1], cache[2], cache[1] + cache[2]


if __name__ == "__main__":

    n = 100
    for i in range(n+1):
        print(count_ways(i))

