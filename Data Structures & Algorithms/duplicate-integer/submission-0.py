class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setList = {0}
        setList.remove(0)
        for i in range(len(nums)):
            if nums[i] in setList:
                return True
            else:
                setList.add(nums[i])
        
        return False
         