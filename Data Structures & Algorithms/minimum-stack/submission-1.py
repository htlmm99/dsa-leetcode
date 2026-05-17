class MinStack:

    def __init__(self):
        self.st = list()
        self.minst = list()

    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.minst:
            self.minst.append(val)
        else:
            if val < self.minst[-1]:
                self.minst.append(val)
            else:
                self.minst.append(self.minst[-1]) 

    def pop(self) -> None:
        self.minst.pop()
        return self.st.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.minst[-1]
