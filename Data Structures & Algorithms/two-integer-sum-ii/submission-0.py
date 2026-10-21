class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numset = set()
        for nums in numbers:
            numset.add(nums)
        
        for i in range(len(numbers)):
            if target - numbers[i] in numset and target - numbers[i] != numbers[i]:
                return [i+1,numbers.index(target-numbers[i])+1]