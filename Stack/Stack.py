from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return f"popped element is {self.container.pop()}"

    def is_empty(self):
        return len(self.container) == 0

    def peek(self):
        return self.container[-1]

if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    print(s.peek())
    print(s.pop())
    print(s.peek())
    print(s.is_empty())

    