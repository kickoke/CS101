"""
Write a program to sort a stack such that the smallest
items are on the top. You can use an additional temporary
stack, but you may not copy the elements into any other
data structure (such as an array). The stack supports the
following operations: push, pop, peek, and is Empty
"""


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return

    def isEmpty(self):
        if len(self.stack) > 0:
            return False
        else:
            return True

    def __len__(self):
        return len(self.stack)


unsorted = Stack()
unsorted.push(9)
unsorted.push(5)
unsorted.push(8)
unsorted.push(2)
unsorted.push(7)
# 9 -> 5 -> 8 -> 2 -> 7

# Since the array needs to be returned in ascending order at the end,
# tmp has to store the numbers in descending order
# tmp 9, 8, 7, 5, 2
# --> 2, 5, 7, 8, 9


def sort_stack(input_stack: Stack) -> Stack:
    # Edge case: Empty or 1 stacks are already sorted
    if len(input_stack) <= 1:
        return input_stack
    tmp = Stack()
    tmp.push(input_stack.pop())

    while not input_stack.isEmpty():
        if input_stack.peek() >= tmp.peek():
            tmp.push(input_stack.pop())

        else:
            smaller = input_stack.pop()
            # push any larger values back onto unsorted
            # while the smaller value keeps being smaller than
            # what's in tmp
            while not tmp.isEmpty() and tmp.peek() > smaller:
                input_stack.push(tmp.pop())
            tmp.push(smaller)

    while not tmp.isEmpty():
        # Copy back to unsorted
        input_stack.push(tmp.pop())

    return input_stack
