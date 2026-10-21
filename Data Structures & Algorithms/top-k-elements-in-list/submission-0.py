class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        result = []

        for i in range(len(nums)):
            dic[nums[i]] += 1
        
        maxNum = 0
        index = 0

        while k != 0:
            for i in range(len(nums)):
                if maxNum < dic[nums[i]]:
                    maxNum = dic.get(nums[i])
                    index = nums[i]

            result.append(index)
            dic.pop(index)
            maxNum = 0
            k-=1
        
        return result
