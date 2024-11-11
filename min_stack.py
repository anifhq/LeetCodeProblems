class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.min_value = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_value == None:
            self.min_value = val
        else:
            if val < self.min_value:
                self.min_value = val
        self.min_stack.append(self.min_value)

    def pop(self) -> None:
        del self.stack[-1]
        del self.min_stack[-1]
        if len(self.stack) == 0:
            self.min_value = None
        else:
            self.min_value = self.min_stack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_value
