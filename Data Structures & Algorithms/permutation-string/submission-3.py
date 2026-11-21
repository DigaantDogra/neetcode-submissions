class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26


# the solution is similar to anagram question but here we are taking the window size == 
# s1 as we exactly want s1 characters from s2. Create 2 hashmaps and for s1 and s2 first 
# of 26 0's and fill both, after that start the window till you find the exact window, 
# while you increase the r increase the number of char at r before increasing r in s2 
# and while increasing the l decrease the number of char that was at l, do this untill 
# you find the exact match. Make a match variable to make it easy as the match will 
# start at 0 and when its value increases to 26 return true at that moment because you 
# should have reached the exact match in s2