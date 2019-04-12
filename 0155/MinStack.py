class MinStack:

    def __init__(self):
        self.data = []
        self.min = []

    def push(self, x: int) -> None:
        min_x = x if not self.min else min(self.min[-1], x)
        self.data.append(x)
        self.min.append(min_x)
        
    def pop(self) -> None:
        self.data.pop()
        self.min.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.min[-1]