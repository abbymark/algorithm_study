class Solution:
    def reverseWords(self, s: str) -> str:
        sps = s.split()
        result = []
        for sp in sps:
            result.append(sp[::-1])
        return ' '.join(result)