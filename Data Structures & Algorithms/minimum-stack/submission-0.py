class MinStack:

    def __init__(self):
        self.values=[]

    def push(self, val: int) -> None:
        self.values.insert(0, val)

    def pop(self) -> None:
        return self.values.pop(0)

    def top(self) -> int:
        return self.values[0]

    def getMin(self) -> int:
        return min(self.values)