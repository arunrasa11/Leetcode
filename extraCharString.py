def minExtraChar(s, dictionary):

    n = len(s)
    dp = [0] * (n+1)    # Initialize an array to store the minimum extra characters.

    for i in range(n - 1, -1, -1):
        dp[i] = 1 + dp[i + 1]  # Initialize with one extra character.

        for w in dictionary:
            if i + len(w) <= n and s[i:i + len(w)] == w:
                dp[i] = min(dp[i], dp[i + len(w)])           # Update if a word in the dictionary is found.

    return dp[0]  # Return the minimum extra characters for the entire string.


s = "leetscode"
dictionary = ["leet", "code", "leetcode"]
print(minExtraChar(s, dictionary))
# Output: 1

s = "sayhelloworld"
dictionary = ["hello", "world"]
print(minExtraChar(s, dictionary))
#Output: 3

s = "arunrajselvaraj"
dictionary = ["arunr", "arun", "selva", "selvaraj", "raj"]
print(minExtraChar(s, dictionary))
#Output: 0

s ="dwmodizxvvbosxxw"
dictionary = ["ox", "lb", "diz", "gu", "v", "ksv", "o", "nuq", "r", "txhe", "e", "wmo", "cehy", "tskz", "ds", "kzbu"]
print(minExtraChar(s, dictionary))
#Output: 9
