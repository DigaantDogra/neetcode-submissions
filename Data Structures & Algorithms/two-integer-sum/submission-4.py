class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_hash = dict()
        
        for i in range(0,len(nums)):
            if (target-nums[i]) in num_hash:
                return [num_hash[target-nums[i]],i]
            else:
                num_hash[nums[i]] = i
