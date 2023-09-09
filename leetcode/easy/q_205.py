class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_list = []
        t_list = []

        for i in s:
            s_list.append(s.index(i))
        
        for i in t:
            t_list.append(t.index(i))
        
        if s_list == t_list:
            return True
        return False