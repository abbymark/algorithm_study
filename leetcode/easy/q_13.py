class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
        }
        r = []
        for i in s:
            r.append(dic[i])
        v = 0
        for n in range(len(r)-1):
            if r[n] >= r[n+1]:
                v += r[n]
            else:
                v -= r[n]
        v += r[-1]
        return v
