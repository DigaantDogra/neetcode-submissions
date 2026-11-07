class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p,s in zip(position,speed)]

        stack = []
        for p,s in sorted(pair)[::-1]: # this will reverse slicing
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)


# we start the problem with reverse and check the (target - p) /s if the number after is 
# smaller than the current then we pop it because that car will eventully become a fleet
# we can also use hash map for p, s 