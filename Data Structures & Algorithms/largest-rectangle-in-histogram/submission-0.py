class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start,h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights)-i ))
        
        return maxArea

# we have to check which height extends towards the right, if the height does not extend 
# towards the right then we pop it as we add the next one or current one.
# make sure to revisit this question when you are not able to still solve with this big hint