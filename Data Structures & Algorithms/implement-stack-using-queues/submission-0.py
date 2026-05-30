class MyStack:

    def __init__(self):
        self.s = 0
        self.t = 0
        self.stack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.t +=1
        

    def pop(self) -> int:
        self.t -= 1
        return self.stack.pop()

        

    def top(self) -> int:
        print(self.t)
        return self.stack[self.t -1]
        

    def empty(self) -> bool:
        return False if self.t else True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()