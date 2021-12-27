def lengthOfLongestSubstring(s: str) -> int:
    dic = {}
    start = 0
    max_length = 0
    cur_length = 0

    for i, letter in enumerate(s):
        if letter in dic and dic[letter] >= start:
            start = dic[letter] + 1
            cur_length = i+1 - start
            dic[letter] = i
            if cur_length > max_length:
                max_length = cur_length
        else:
            dic[letter] = i
            cur_length += 1
            if cur_length > max_length:
                max_length = cur_length
    
    return max_length

print(lengthOfLongestSubstring("tmmzuxt"))
print(lengthOfLongestSubstring("abba"))
print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("a"))
# print(lengthOfLongestSubstring(" "))
# print(lengthOfLongestSubstring(""))