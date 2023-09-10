def solution(s):
    n = len(s)
    if n < 3 or n > 100:
        return None

    len_a = 1
    len_b = 1
    len_c = n - len_a - len_b

    count = 0

    while len_a <= n - 2:
        a = s[:len_a]
        b = s[len_a:len_a + len_b]
        c = s[-len_c:]
        if a + b != b + c and a + b != c + a and b + c != c + a:
            count += 1
        len_b += 1
        len_c -= 1
        if len_c == 0:
            len_a += 1
            len_b = 1
            len_c = n - len_a - len_b

    return count

s="xzxzx"
print(solution(s))