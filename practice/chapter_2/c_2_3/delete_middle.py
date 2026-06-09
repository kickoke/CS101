"""
Implement an algorithm to delete a node in the middle of a linked list.
Middle means any node exept the head or tail node.
Do this for a singly linked list
You are only given access to that node

Example:

node c from this linked list: a -> b -> c -> d -> e -> f
Result: a -> b -> d -> e -> f

Nothing returns

---
Hint: Picture the list 1->5->9->12. Removing 9 would make it look like 1->5->12. You only
have access to the 9 node. Can you make it look like the correct answer? 

"""


class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def delete(node: Node) -> None:
    if not node or not node.next:
        raise Exception("Can't delete since not a middle node")
    node.data = node.next.data
    node.next = node.next.next
