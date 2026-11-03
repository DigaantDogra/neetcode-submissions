class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tokStack = []
        opera = {"+","-","/","*"}

        for i in tokens:
            if i not in opera:
                tokStack.append(i)
            else:
                second = int(tokStack.pop())
                first = int(tokStack.pop())
                match i:
                    case "+":
                        tokStack.append(first+second)
                    case "-":
                        tokStack.append(first-second)
                    case "*":
                        tokStack.append(first*second)
                    case "/":
                        tokStack.append(first/second)
        
        return int(tokStack.pop())
        