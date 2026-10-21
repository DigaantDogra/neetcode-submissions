class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        
        sdic = {}
        tdic = {}

        for i in range(len(s)):
            if s[i] not in sdic:
                sdic[s[i]] = 0
            else:
                sdic[s[i]] += 1
            if t[i] not in tdic:
                tdic[t[i]] = 0
            else:
                tdic[t[i]] += 1
        
        if (sdic == tdic):
            return True
        return False