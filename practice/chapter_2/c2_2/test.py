# Setup nodes
from kth_item import get_kth

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from linked_list import Node

node_a = Node("A")
node_b = Node("B")
node_c = Node("C")
node_d = Node("D")

# Link nodes
node_a.next = node_b
node_b.next = node_c
node_c.next = node_d


def test_getkth():
    assert get_kth(node_a, 2) == node_b


def test_too_long():
    assert get_kth(node_a, 5) == None
