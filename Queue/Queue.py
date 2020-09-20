from collections import deque

class Queue:
    def __init__(self):
        self.Q = deque()

    def enqueue(self, val):
        self.Q.appendleft(val)

    def dequeue(self):
        return self.Q.pop()

    def is_empty(self):
        return len(self.Q) == 0

    def size(self):
        return len(self.Q)

if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    print(q.size())
    print(q.dequeue())
    print(q.size())