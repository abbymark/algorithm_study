class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = ""
        for i in s:
            if i.isalpha() or i.isdigit():
                ns += i.lower()
        if ns == ns[::-1]:
            return True
        else:
            return False