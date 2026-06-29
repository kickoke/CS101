"""
Queue via Stacks: Implement a MyQueue class which
implements a queue using two stacks.
---
Idea:
The stack inserts elements one after the other so
that LIFO property is maintained at stack[-1].
The queue inserts the same elements in reverse order,
so that FIFO property is maintained at queue[-1].

Insertions for queue are slow, since the elements
have to be shifted every time at insertion.
"""


class MyQueue:
    def __init__(self):
        self.stack = []
        self.queue = []

    def enqueue(self, item):
        self.stack.append(item)

    def dequeue(self):
        if len(self.queue) == 0:
            while len(self.stack) > 0:
                item = self.stack.pop()
                self.queue.append(item)
        return self.queue.pop()

    def peek(self):
        if len(self.queue) == 0:
            return "No items in the queue"
        return self.queue[-1]
