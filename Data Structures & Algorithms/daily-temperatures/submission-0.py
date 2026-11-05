class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        tempStack = [] # [temp,index]

        for i,t in enumerate(temperatures):
            while tempStack and t > tempStack[-1][0]:
                temp, index = tempStack.pop()
                res[index] = i - index
            tempStack.append([t,i])
        
        return res

# this concept is monotonic decreasing stack, eg 21->20->19 then if something comes
# 21<a, then we start poping and the poped index in then result array
# will be a-(poped index)