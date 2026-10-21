class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsSet = set(nums)
        result = []

        for i in range(len(nums)):
            if target - nums[i] in numsSet and i != nums.index(target - nums[i]):
                return [min(i,nums.index(target - nums[i])),max(i,nums.index(target - nums[i]))]
        
        