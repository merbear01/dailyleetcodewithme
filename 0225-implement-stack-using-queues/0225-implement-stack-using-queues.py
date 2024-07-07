class MyStack(object):

    def __init__(self):
        self.element = []
        

    def push(self, x):
        self.element.append(x)
        

    def pop(self):
        return self.element.pop()
        

    def top(self):
        return self.element[-1]
        

    def empty(self):
        return len(self.element) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()