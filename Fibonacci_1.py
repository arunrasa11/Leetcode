def fib(n:int) -> int:

    fib_series = [0, 1]
    for i in range(2, n):

        # fib_series.append(recur(i, fib_series))
        # fn = lambda x, cache: cache[x-1] + cache[x-2]
        # fib_series.append(fn(i, fib_series))

        fib_series.append((lambda x, cache: cache[x - 1] + cache[x - 2])(i, fib_series))

    return fib_series[n-1]


# def recur(n: int, cache: list) -> int:
#
#     return cache[n-1] + cache[n-2]


def fib1(n: int) -> int:

    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)


if __name__ == "__main__":

    # fib = [0,1,1,2,3,5,8,13,21,34,55]
    n = 30
    print(fib(n))
    print(fib1(n))








