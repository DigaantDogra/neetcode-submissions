class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            
            l, r = i+1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a,nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res

# first of all this will take another try for you to understand well
# in this sol we need to keep 3 var a,l,r where 'a' will be visited only once per copy of a
# value then a will only go till < 0 because l and r will cover all the remaing values
# then we need to sort this first as this is related to two sum 1 and 2, after that try solving this again with this knowledge and if still not able to do it then check and understand the sol again

            