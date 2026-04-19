from binary_tree_pointer import *
import pytest


def test_creation():
    t = Tree()
    assert t.root_node == None


def test_lookup_fails_on_empty_tree():
    t = Tree()
    with pytest.raises(KeyError):
        t.lookup("foo")


def test_first_insert_on_empty_tree():
    t = Tree()
    t.insert("foo", "bar")
    assert type(t.root_node) == Node
    assert t.root_node.key == "foo"
    assert t.root_node.value == "bar"
    assert t.root_node.left == None
    assert t.root_node.right == None


def test_lookup_after_first_insert():
    t = Tree()
    key = "foo"
    value = "bar"
    other_key = "apple"
    t.insert(key, value)
    assert t.lookup(key) == value
    with pytest.raises(KeyError):
        t.lookup(other_key)


def test_mulitple_inserts():
    values = [
        ("pear", 5),
        ("banana", 10),
        ("pineapple", 21),
        ("apple", 33),
        ("strawberry", 12),
    ]
    t = Tree()
    for value in values:
        t.insert(value[0], value[1])

    for value in values:
        assert t.lookup(value[0]) == value[1]

    assert t.root_node.key == "pear"
    assert t.root_node.left.key == "banana"
    assert t.root_node.right.key == "pineapple"
    assert t.root_node.left.left.key == "apple"
    assert t.root_node.left.right == None
    assert t.root_node.right.left == None
    assert t.root_node.right.right.key == "strawberry"


def test_existing_node_overwrite():
    values = [
        ("pear", 5),
        ("banana", 10),
        ("pineapple", 21),
        ("apple", 33),
        ("strawberry", 12),
    ]
    t = Tree()
    for value in values:
        t.insert(value[0], value[1])
    with pytest.raises(KeyError):
        t.insert("pear", 1)
        t.insert("strawberry", 2)


"""
def test_delete_leaf_from_3_node_tree():
    values = [
        ("pear", 5),
        ("banana", 10),
        ("pineapple", 21),
    ]
    t = Tree()
    for value in values:
        t.insert(value[0], value[1])

    assert t.root_node.left.key == "banana"
    t.delete("banana")
    assert t.root_node.left == None

    assert t.root_node.right.key == "pineapple"
    t.delete("pineapple")
    assert t.root_node.right == None


def test_delete_leaf_from_5_node_tree():
    values = [
        ("pear", 5),
        ("banana", 10),
        ("pineapple", 21),
        ("apple", 33),
        ("strawberry", 12),
    ]
    t = Tree()
    for value in values:
        t.insert(value[0], value[1])
    assert t.root_node.right.right.key == "strawberry"
    assert t.root_node.left.left.key == "apple"

    t.delete("strawberry")
    t.delete("apple")

    assert t.root_node.right.right == None
    assert t.root_node.left.left == None
"""


def test_delete_node_one_child():
    values = [9, 5, 15, 3]
    t = Tree()
    for value in values:
        t.insert(value, value)

    assert t.root_node.left.key == 5
    assert t.root_node.left.left.key == 3
    assert t.root_node.left.right == None

    t.delete(5)

    assert t.root_node.left.key == 3
    assert t.root_node.left.left == None
    assert t.root_node.left.right == None


"""
from binary_tree import BinarySearchTree


items_list = [
    4,
    2,
    5,
    2,
    7,
    8,
    9,
    0,
    7,
    5,
    4,
    232,
    5,
    4534,
    332,
    12124,
    432,
    124,
    543,
    654,
    12,
    5672213,
    432,
    563,
    76,
    765,
    2352,
    724,
]
items_tuple = (
    4,
    2,
    5,
    4,
    232,
    5,
    4534,
    332,
    12124,
    432,
    124,
    543,
    654,
    12,
    432,
    563,
    76,
    765,
    2352,
    724,
)

items_string = "AKEHDUWJFOXNKFHEYI"
items_list_string = ["apple", "banana", "orange", "nut", "peach", "cherry", "cocoa"]

tree = BinarySearchTree()

for item in items_list:
    tree.insert(item)

print(tree)


"""
