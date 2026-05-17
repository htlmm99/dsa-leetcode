class MinStack:

    def __init__(self):
        self.st = list()
        self.min=999999999

    def push(self, val: int) -> None:
        self.st.append(val)
        if val < self.min:
            self.min = val

    def pop(self) -> None:
        return self.st.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return min(self.st)
