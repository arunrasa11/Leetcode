from collections import Counter, defaultdict


def perm_palindrome(str):
    c = Counter(str)

    num_odds = 0

    print(c)
    for char, count in c.items():
        if count % 2 != 0:
            num_odds += 1

    return num_odds <= 1

str = 'cacerra'
def perm_palindrome1(str):

        if len(str) % 2 == 0:
            return len(str) == 2 * len(set(str))
        else:
            return len(str) == 2 * len(set(str)) - 1

# print(perm_palindrome1(str))


def perm_palindrome_arun(str):

    word_dict = defaultdict(int)
    for char in str:
        word_dict[char] += 1

    odd_count = 0
    for val in word_dict.values():
        if val % 2 != 0:
            odd_count += 1
            if odd_count > 1:
                return False
    return True

print(perm_palindrome_arun(str))




