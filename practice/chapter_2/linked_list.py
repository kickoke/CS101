"""
Pro: O(1) for adding at the top
"""


class Node:
    """
    Node class that supports doubly linked lists.
    """

    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def get(self):
        return self.data

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set(self, d):
        self.data = d
        return self.data

    def update_next(self, node):
        self.next = node
        return self.next

    def update_prev(self, node):
        self.prev = node
        return self.prev
