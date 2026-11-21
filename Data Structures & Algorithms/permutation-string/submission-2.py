class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashT = dict()

        n = 0
        s1Count,s2Count = 0,len(s2)

        for i in s1:
            hashT[i] = hashT.get(i, 0) + 1
            s1Count += 1
        
        for i in range(s2Count):
            if s2[i] in hashT:
                n = i
                dup = hashT.copy()
                while (n - i) < s1Count and n < s2Count:
                    if s2[n] in dup:
                        if dup[s2[n]] >= 1:
                            dup[s2[n]] -= 1
                        if dup[s2[n]] == 0:
                            del dup[s2[n]]
                        n += 1
                    else:
                        break
                if not dup:
                    return True
        
        return False
