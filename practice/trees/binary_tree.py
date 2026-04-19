"""
Binary tree is a tree with:
* One root node
* Left side: smaller than the current
* Right side: larger than the current node
* Leaf nodes (no nodes after it)

Important: Unlike a min heap or a max heap, the root node can be any value.
This implementation uses an array as the underlying stoarge and heap-like logic
to build the array. Instead of satisfying the heap invariant, I aim to satisfy the BST invariant.

Operations:

Traversal:
The tree can be traversed in 4 ways, all are O(n):
* pre order traversal (depth first search, from top): Recursive visiting from root-->left-->right, starting with the left subtree. Useful for copying a tree.
* in order traversal: Yields a sorted output from smallest to largest (ascending)
* post order traversal(depth first search, from bottom): Recursive visiting from left-->right-->root, starting with the left subtree. Useful for deleting a tree.
* level order traversal (breadth first search): Yields output of each level

Insert

Delete

Check height

Contains element (lookup)
"""

from collections.abc import Iterable
import math


class BinarySearchTree:
    """
    Creates a BinarySearchTree object. Supported types are any thata allow for indexing, like list, string, tuple.
    Not allowed: Sets, dicts, generators, iterators
    Methods:
    * insert
    * delete
    * contains
    _str_ (print in a certain traversal order)
    """

    def __init__(self) -> None:
        self.tree = [None]
        self.nodes = len(self.tree)
        self.height = math.floor(math.log2(len(self.tree))) + 1
        self.width = (2 ^ self.height) - 1  # Total width
        self.root = self.tree[0]

    def __str__(self):
        return self.tree

    """
    Insert node
    """

    def insert(self, value, current_node=0):
        """
        Inserts a new node relative to the current node.
        # Check out of bounds
        """
        # Edge case: Construct root
        # If none, then write
        if self.tree[current_node] == None:
            self.tree[current_node] = value
            if len(self.tree) == 1:
                self.tree.extend([None] * 2)  # Placeholder for child nodes
            return

        # Insert to the left
        if value < self.tree[current_node]:
            i = 2 * current_node + 1
            if i >= len(self.tree):
                self.tree.extend([None] * (i - len(self.tree)))
            return self.insert(value, i)

        if value > self.tree[current_node]:
            i = 2 * current_node + 2
            if i >= len(self.tree):
                self.tree.extend([None] * (i - len(self.tree)))
            return self.insert(value, i)

    def rebalance(self, tree):
        """Function to rebalance the BST"""
        # Traverse in order
        # Pick median as new root
        # recursively build left and right sides

    """
    Delete node
    """

    def delete(self, value):
        """
        If node is present, delete it.
        """
        n = self._contains(value)
        if n == False:
            raise ValueError(f"No node with {value} in tree")
        else:
            self.tree[n] = None
        return

    """
    Traversal
    """

    def preorder_traverse(self, index):
        if index >= len(self.tree) or self.tree[index] is None:
            return []
        return (
            [self.tree[index]]
            + self.preorder_traverse(self.get_left_child(index))
            + self.preorder_traverse(self.get_right_child(index))
        )

    def inorder_traverse(self, index):
        if index >= len(self.tree) or self.tree[index] is None:
            return []
        return (
            self.inorder_traverse(self.get_left_child(index))
            + [self.tree[index]]
            + self.inorder_traverse(self.get_right_child(index))
        )

    def postorder_traverse(self, index):
        if index >= len(self.tree) or self.tree[index] is None:
            return []
        return (
            self.postorder_traverse(self.get_left_child(index))
            + self.postorder_traverse(self.get_right_child(index))
            + [self.tree[index]]
        )

    def level_order_traverse(self):
        """Returns values of each level"""
        result = []
        if self.tree[0] is None:
            return []
        for node in self.tree:
            if node is not None:
                result.append(node)
        return result

    """
    Search
    """

    def contains(self, query, current_node=0) -> bool | None:
        """Checks if the element is in the tree"""
        # Base case: End of the branch
        if current_node == None:
            return False
        # Case: match found
        if query == self.tree[current_node]:
            return True
        # Check left subtree
        if query < self.tree[current_node]:
            return self.contains(query, self.get_left_child(current_node))
        # Check right subtree
        if query > self.tree[current_node]:
            return self.contains(query, self.get_right_child(current_node))

    def _contains(self, query, current_node=0) -> int | bool | None:
        """Checks if the element is in the tree and returns its index"""
        # Base case: End of the branch
        if current_node == None:
            return False
        # Case: match found
        if query == self.tree[current_node]:
            return current_node
        # Check left subtree
        if query < self.tree[current_node]:
            return self.contains(query, self.get_left_child(current_node))
        # Check right subtree
        if query > self.tree[current_node]:
            return self.contains(query, self.get_right_child(current_node))

    """
    Helper functions
    """

    def get_left_child(self, index_current_node: int) -> int:
        """
        Get the left node index of the current node
        """
        return 2 * index_current_node + 1

    def get_right_child(self, index_current_node: int) -> int:
        """
        Get the right node index of the current node
        """
        return 2 * index_current_node + 2

    def get_parent(self, index_current_node):
        return math.floor((index_current_node - 1) / 2)
