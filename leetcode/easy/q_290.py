class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split()
        
        pattern_index_list=[]
        s_index_list = []

        for p in pattern:
            pattern_index_list.append(pattern.index(p))
        
        for s_ in s_list:
            s_index_list.append(s_list.index(s_))

        if pattern_index_list == s_index_list:
            return True
        return False