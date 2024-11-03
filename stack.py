class Stack:
    def __init__(self) -> None:
        self.st = []

    def size(self):
        return len(self.st)
    
    def push(self, x):
        self.st.append(x)

    def pop(self):
        if len(self.st) > 0:
            return self.st.pop()
        else:
            raise IndexError("pop from empty stack")

    def top(self):
        if len(self.st) > 0:
            return self.st[-1]
        else:
            raise IndexError("top from empty stack")

    def isempty(self):
        return len(self.st) == 0
