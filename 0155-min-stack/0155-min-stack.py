class MinStack(object):

    def __init__(self):
        self.element = []
        

    def push(self, val):
        self.element.append(val)
        

    def pop(self):
        self.element.pop()
        

    def top(self):
        return self.element[-1]
        

    def getMin(self):
        return min(self.element)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()