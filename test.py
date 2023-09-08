from collections import defaultdict
def minExtraChar(s, dictionary):

    n = len(s)
    word_dict = defaultdict(list)

    for word in dictionary:
        word_dict[word[0]].append(word)

    result = [0] * (n + 1)

    for i in range(n - 1, -1, -1):
        result[i] = result[i + 1] + 1
        if s[i] in word_dict:
            for word in word_dict[s[i]]:
                if s[i:i + len(word)] == word:
                    result[i] = min(result[i], result[i + len(word)])

    return result[0]


s = "arunrajselvaraja"
dictionary = ["arunr", "arun", "selva", "selvaraj", "raj"]
print(minExtraChar(s, dictionary))
#Output: 0