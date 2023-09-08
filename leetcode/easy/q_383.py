class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = sorted(ransomNote)
        magazine = sorted(magazine)

        ransom_p = 0
        mag_p = 0

        for i in range(len(magazine)):
            if ransomNote[ransom_p] == magazine[mag_p]:
                ransom_p += 1
                mag_p += 1
            else:
                mag_p += 1
            if len(ransomNote) == ransom_p:
                return True
        return False