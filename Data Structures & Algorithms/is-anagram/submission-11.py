class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sHash = dict(Counter(s))
        tHash = dict(Counter(t))
        
        if tHash == sHash:
            return True
        else:
            return False
