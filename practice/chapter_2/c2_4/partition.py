"""
Write code to partition a linked list around value x. 
All nodes smaller than x should come before x and 
all greater than or equal to should come after.

If x is contained, the values of x only need to be after the elements less than x. 
The partition element can appear anywhere in the right half.

Example:
3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

---
From the example, it looks like a singly linked list?
1. Traverse list and compare against partition value.
2. 
"""




class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next



def partition(node, x):
    if not node:
        return
    current_node = node
    less_than_partition = Node("HEAD: Less than x")
    greater_than_partition = Node("HEAD: Greater than x")
    less_than_partition_tail = None
    greater_than_partition_tail = None

    while current_node:
        next_node = current_node.next

        if current_node.data < x:
            if less_than_partition_tail is None:
                less_than_partition_tail = current_node
            current_node.next = less_than_partition.next
            less_than_partition.next = current_node
    
        if current_node.data >= x:
            if greater_than_partition_tail is None:
                greater_than_partition_tail = current_node
            current_node.next = greater_than_partition.next
            greater_than_partition.next = current_node
        
        current_node = next_node

    # Merge two lists together again by checking if left/right have values
    if less_than_partition_tail:
        less_than_partition_tail.next = greater_than_partition.next

    if greater_than_partition.next: 
        greater_than_partition = greater_than_partition.next


