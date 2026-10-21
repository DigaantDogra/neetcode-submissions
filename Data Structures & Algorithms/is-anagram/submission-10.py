class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sHash = dict(Counter(s))
        tHash = dict(Counter(t))

        for i in s:
            sHash[i] += 1

        for i in t:
            tHash[i] += 1
        
        if tHash == sHash:
            return True
        else:
            return False
