class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return str(self.stack)

    def push(self, key):
        self.stack = self.stack + [key]

    def pop(self):
        if self.empty():
            return None
        key_to_pop = self.stack[-1]
        self.stack = self.stack[:-1]
        return key_to_pop

    def empty(self):
        return len(self.stack) == 0
