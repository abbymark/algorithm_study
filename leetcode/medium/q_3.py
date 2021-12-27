def lengthOfLongestSubstring(s: str) -> int:
    dic = {}
    start = 0
    max_length = 0
    cur_length = 0

    for i, letter in enumerate(s):
        # breakpoint()
        if letter not in dic:
            dic[letter] = i
            cur_length += 1
            if max_length < cur_length:
                max_length = cur_length
        else:
            dic[letter] = i
            start = i + 1
            if max_length <i+1-start:
                max_length=i+1-start
            cur_length = 0
        
    return max_length

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("a"))
# print(lengthOfLongestSubstring(" "))
# print(lengthOfLongestSubstring(""))