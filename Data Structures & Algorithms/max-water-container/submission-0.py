class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0

        l, r = 0, len(heights) - 1

        while l < r:
            area = max(area, (min(heights[l], heights[r]) * (r-l)))

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
                r -= 1
            
        return area

# 2 pointers one at right end one at left end if left is small increase l if right is small 
# decrease r, and with this do max for the area produces as that will keep the max area 
# found while you visit every node
        