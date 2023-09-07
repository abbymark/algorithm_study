class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        s_p= 0
        t_p = 0
        for i in t:
            if len(s) != s_p and s[s_p] == t[t_p]:
                s_p += 1
                t_p += 1
            else:
                t_p += 1
        if s_p == len(s):
            return True
        return False