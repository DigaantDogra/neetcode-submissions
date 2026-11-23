class Solution:
    def minWindow(self, s: str, t: str) -> str:
        slen, tlen = len(s), len(t)

        l, r = 0,0
        have, need = 0,0
        tVal, sVal = {}, {}

        res, minLen = [-1,-1], float("infinity")

        for i in t:
            tVal[i] = 1 + tVal.get(i,0)
            need += 1
        
        while r < slen:
            if s[r] in tVal:
                sVal[s[r]] = sVal.get(s[r],0) + 1
                if sVal[s[r]] <= tVal[s[r]]:
                    have += 1
                while have == need:
                    if minLen > (r-l+1):
                        minLen = r-l+1
                        res = [l,r]
                    if s[l] in tVal:
                        sVal[s[l]] -= 1
                        if sVal[s[l]] < tVal[s[l]]:
                            have -= 1
                    l += 1
            r += 1

        
        return s[res[0]:res[1]+1] if minLen != float("infinity") else ""
                

