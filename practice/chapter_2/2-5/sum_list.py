"""
You have two numbers represented by a linked list where 
each node contains a single digit. The digits are stored 
in reverse order, such that the 1's digit is at the head 
of the list. Write a function that adds the two numbers 
and returns the sum as a linked list.

Example: (7 -> 1 -> 6) + (5 -> 9 -> 2) that is 617 + 295
Output: 2 -> 1 -> 9 that is 912
---
Reversed order from smallest to largest means that I can simply traverse forward.
I can sum up the 1's place, the 10's place and so on. I do need to pay attention 
to the carryover and apply it to the next node.

What if we sum up two lists of different lengths?
-> Looping logic can basically stop work after the carryover 
has been applied and the shorter list has been processed.

Since we are summing up 2 ints or floats, we would need to do 
typechecking for x.data and y.data. 
I will skip this in the interest of time.
"""


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def sum_lists(x: Node, y: Node) -> Node:
    sum_head = Node()
    sum = sum_head
    carryover = 0
    current_x = x
    current_y = y

    while current_x is not None or current_y is not None or carryover > 0:
        # Get the current values, defaulting to 0 if the node is None
        val_x = current_x.data if current_x is not None else 0
        val_y = current_y.data if current_y is not None else 0
        # Summation logic
        tmp_sum = tmp_sum = val_x + val_y + carryover
        # reset carryover after adding
        if carryover != 0:
            carryover = 0

        carryover = tmp_sum // 10 
        sum.next = Node(tmp_sum % 10)
        sum = sum.next

        if current_x is not None:
            current_x = current_x.next
        if current_y is not None:
            current_y = current_y.next
    
    return sum_head.next



