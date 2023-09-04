class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cp = ""
        temp_cp = ""
        for s in strs[0]:
            temp_cp += s
            flag = False
            if all([temp_cp in string[:len(temp_cp)] for string in strs]):
                cp = temp_cp
            else:
                break
        return cp