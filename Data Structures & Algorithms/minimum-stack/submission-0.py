class MinStack:

    def __init__(self):
        self.nodeList = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.nodeList.append(val)
        if not self.minStack:
            self.minStack.append(self.nodeList[-1])
        else:
            self.minStack.append(min(self.minStack[-1],self.nodeList[-1]))
 
    def pop(self) -> None:
        self.nodeList.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.nodeList[-1]

    def getMin(self) -> int:
        if not self.minStack:
            return None
        
        return self.minStack[-1]
