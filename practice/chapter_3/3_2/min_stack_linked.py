"""
Design a stack that has a push, pop and min() function.
All of them should return in O(1) time.
"""


class Node:
    def __init__(self, value, min_so_far):
        self.value = value
        self.min_so_far = min_so_far
        self.next = None


class MinStack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, item):
        if not self.head:
            # If the stack is empty, the item itself is the minimum so far
            current_min = item
        else:
            # Otherwise, compare the new item with the min of the current head
            current_min = min(item, self.head.min_so_far)

        # Create the new node with its snapshot min
        next_item = Node(item, current_min)

        # Link new node to old head, then move head to the new node
        next_item.next = self.head
        self.head = next_item
        self.size += 1

    def pop(self):
        if not self.head:
            return "Stack is empty"
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.value

    def peek(self):
        if not self.head:
            return "Stack is empty"
        return self.head.value

    def StackMin(self):
        if not self.head:
            return "Stack is empty"
        return self.head.min_so_far

    def stackSize(self):
        return self.size
