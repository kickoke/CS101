"""
Write code to remove duplicates from an unsorted linked list.

Hint: Have you tried a hash table?

Follow up: How would you solve this if a temporary buffer is not allowed?
---
Specify: Singly or doubly linked list? Let's do doubly since singly is a subset of doubly, just ignoring prev.
"""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from linked_list import Node


def remove_dupe_singly(linked_list: Node) -> Node:
    if not isinstance(linked_list, Node):
        raise TypeError("Please provide the head node of a linked list.")

    unique_nodes = set()  # Using a set is faster if you only need to look up keys
    prev_node = None
    current_node = linked_list

    while current_node:
        if current_node.get() not in unique_nodes:
            unique_nodes.add(current_node.get())
            prev_node = current_node  # Move prev forward only for unique nodes
        else:
            if prev_node:
                prev_node.update_next(current_node.get_next())

        current_node = current_node.get_next()

    return linked_list


def remove_dupe_doubly(linked_list: Node) -> Node:
    if not isinstance(linked_list, Node):
        raise TypeError("Please provide the head node of a linked list.")

    unique_nodes = set()
    current_node = linked_list

    while current_node:
        next_node = current_node.get_next()

        if current_node.get() not in unique_nodes:
            unique_nodes.add(current_node.get())
        else:
            prev_node = current_node.get_prev()

            if prev_node:
                prev_node.update_next(next_node)
            if next_node:
                next_node.update_prev(prev_node)

        current_node = next_node

    return linked_list
