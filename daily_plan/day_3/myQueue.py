class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.queue_stack = []

    def push(self, x: int) -> None:
        while(self.queue_stack):
            element = self.queue_stack.pop()
            self.in_stack.append(element)
        self.queue_stack.append(x)
        while(self.in_stack):
            element = self.in_stack.pop()
            self.queue_stack.append(element)


    def pop(self) -> int:
        element = self.queue_stack.pop()
        return element

    def peek(self) -> int:
        element = self.queue_stack.pop()
        self.queue_stack.append(element)
        return element

    def empty(self) -> bool:
        if(len(self.queue_stack) < 1): return True
        return False