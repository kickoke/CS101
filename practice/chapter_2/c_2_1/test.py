from remove_dupes import remove_dupe_singly
from linked_list import Node

"""
These tests were such a pain so I decided to skip _doubly
"""


# Use functions to generate FRESH lists for every single test case
def make_duplicates_list():
    # 1 -> 2 -> 3 -> 2 -> 4 -> 1 -> 5
    head = Node(1)
    head.update_next(Node(2))
    head.get_next().update_next(Node(3))
    head.get_next().get_next().update_next(Node(2))
    head.get_next().get_next().get_next().update_next(Node(4))
    head.get_next().get_next().get_next().get_next().update_next(Node(1))
    head.get_next().get_next().get_next().get_next().get_next().update_next(Node(5))
    return head


def make_after_deletion_list():
    # 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.update_next(Node(2))
    head.get_next().update_next(Node(3))
    head.get_next().get_next().update_next(Node(4))
    head.get_next().get_next().get_next().update_next(Node(5))
    return head


def make_no_duplicates_list():
    # 10 -> 20 -> 30 -> 40 -> 50
    head = Node(10)
    head.update_next(Node(20))
    head.get_next().update_next(Node(30))
    head.get_next().get_next().update_next(Node(40))
    head.get_next().get_next().get_next().update_next(Node(50))
    return head


# Helper function to convert the items to a list
def to_list(head):
    result = []
    current = head

    while current:
        result.append(current.get())
        current = current.get_next()

    return result


def test_deletion():
    duplicates = make_duplicates_list()
    after_deletion = make_after_deletion_list()
    assert to_list(remove_dupe_singly(duplicates)) == to_list(after_deletion)


def test_no_deletion():

    no_duplicates = make_no_duplicates_list()

    returned_node = remove_dupe_singly(no_duplicates)
    print("\nDEBUG - Returned Node:", returned_node)

    assert to_list(returned_node) == to_list(no_duplicates)
