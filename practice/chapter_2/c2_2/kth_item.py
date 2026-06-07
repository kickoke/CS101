"""
Implement an algorithm to find the kth to the last element of a singly linked list
---
Last element is current.next = None
kth means distance between current and kth.
1. initialize kth trailing pointer with none
2. count how often current has been advanced.
3. when current.next is not yet none and has met the threshold for k, advance both pointers
4. When current.next = None, we have reached the end of the list. Return the current_k node
-->
"""


def get_kth(head, k):
    # If we knew that the linked list is shorter than k we could return early...

    current_k = None
    current_node = head
    traversal_count = 0

    # Traverse from head to tail
    while current_node:
        if traversal_count == k:
            current_k = head
        if traversal_count > k:
            current_k = current_k.get_next()
        current_node = current_node.get_next()
        traversal_count = traversal_count + 1

    return current_k
