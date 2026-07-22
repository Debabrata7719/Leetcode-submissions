class MyQueue:

    def __init__(self):
        self.values=[]
        

    def push(self, x: int) -> None:
        self.values=[x]+self.values

    def pop(self) -> int:
        return self.values.pop()

    def peek(self) -> int:
        return self.values[-1]

    def empty(self) -> bool:
        return len(self.values)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()