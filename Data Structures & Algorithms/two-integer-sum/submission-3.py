class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_hash = dict()

        for i in range(0,len(nums)):
            num_hash[nums[i]] = i
        
        for i in range(0,len(nums)):
            if (target-nums[i]) in num_hash and i != num_hash[target-nums[i]]:
                return [i, num_hash[target-nums[i]]] 
        
        return [0,0]
