"""
Design a stack that has a push, pop and min() function.
All of them should return in O(1) time.
---
We can basically store the current min in a variable.
We need to store min in a way that we know what the previous min was,
if the current min is deleted.
Data structures: Since I am building a stack data structure,
for a clean implementation I can just maintain a second min
stack inside the data structure.

Example:

Base case: stack of len 1 --> min == item in stack

Extreme case 1: Each next value is smaller than the one before:
5 | 4 | 3 | 2 | 1 | 0
--> need to update min every time we append a new item.
--> original stack and min stack are the same & we are wasting space

Extreme case 2: Sorted input:

1 | 2 | 3 | 4 | 5 | 6 | 7
--> Here a simple var would be sufficient.
A small min stack of len 1 would still be okay in terms of space I guess.

Case:
mins are mixed into the input
5 | 6 | 4 | 7 | 3 | 8 | 2 | 9
--> Here, the min stack would look like this:
5 | 4 | 3 | 2

Edge case: Same sequence of numbers:
5 | 5 | 3
--> Min stack would be empty after popping 3, 5 although min stack should still contain 5
"""


class Min_stack:
    def __init__(self):
        self.stack = []
        self.minimum = []

    def push(self, item):
        if len(self.minimum) == 0 or item <= self.minimum[-1]:
            self.minimum.append(item)
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return None
        if self.stack[-1] == self.minimum[-1]:
            self.minimum.pop()
        self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def min(self):
        if len(self.minimum) == 0:
            return None
        return self.minimum[-1]
