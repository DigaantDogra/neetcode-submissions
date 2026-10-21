class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        pre = []
        post = []

        temp = 1
        post.append(temp)
        for i in range(0,len(nums)-1):
            temp *= nums[i]
            post.append(temp)

        temp = 1
        pre.append(temp)
        for i in range(len(nums)-1,0,-1):
            temp *= nums[i]
            pre.append(temp)
        
        i = 0
        j = len(nums)-1
        while i<len(nums):
            res.append(pre[j]*post[i])
            i+=1
            j-=1
        
        return res
            