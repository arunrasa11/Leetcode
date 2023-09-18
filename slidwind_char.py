def lengthOfLongestSubstring(s: str) -> int:

    if len(s) == 0:
        return 0

    substr = ''
    max1 = 0

    for char in s:
        if char not in substr:
            substr += char
        else:
            max1 = max(len(substr), max1)
            idx = substr.index(char)
            substr = substr[idx + 1:] + char

    max1 = max(len(substr), max1)
    return max1


s = "vdvf"
print(lengthOfLongestSubstring(s))