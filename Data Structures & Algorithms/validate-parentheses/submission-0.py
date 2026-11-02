class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")":"(", "}":"{", "]":"["}

        for string in s:
            if string == "(" or string == "{" or string == "[":
                stack.append(string)
                continue
            if stack and stack[-1] == closeToOpen[string]:
                stack.pop()
            else:
                return False
        
        return True if not stack else False
            