# Class node
class Node:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def has_only_left(self):
        return self.left and not self.right

    def has_only_right(self):
        return self.right and not self.left

    def has_two_children(self):
        return self.left and self.right


# Class tree
class Tree:
    def __init__(self) -> None:
        self.root_node = None

    def _insert(self, node, key, value):
        if key < node.key:
            if node.left:
                return self._insert(node.left, key, value)
            node.left = Node(key, value)
        elif key > node.key:
            if node.right:
                return self._insert(node.right, key, value)
            node.right = Node(key, value)
        else:
            raise KeyError("Key already exists.")

    def insert(self, key, value):
        if self.root_node == None:
            self.root_node = Node(key, value)
            return
        return self._insert(self.root_node, key, value)

    def _lookup(self, node, key):
        if node == None:
            raise KeyError("Key not in tree.")
        if key == node.key:
            return node.value
        elif key < node.key:
            return self._lookup(node.left, key)
        elif key > node.key:
            return self._lookup(node.right, key)

    def lookup(self, key):
        return self._lookup(self.root_node, key)

    def _delete(self, node, key): ...

    def delete(self, key):
        """Check empty tree"""
        if self.root_node == None:
            raise KeyError("No entries in tree.")
        """Delete root node"""
        elif key == self.root_node.key:
            old_root = self.root_node
            self.root_node = None
            self._insert_tree(old_root.left)
            self._insert_tree(old_root.right)

        """Delete node with one child (left)"""
        elif key < self.root_node.key:
            if key == self.root_node.left.key:
                if self.root_node.left.has_only_left():
                    self.root_node.left = self.root_node.left.left
                elif self.root_node.left.has_only_right():
                    self.root_node.left = self.root_node.left.right
                elif self.root_node.left.has_two_childen():
                    temp_tree = self.root_node.left.left
                    self.root_node.left = self.root_node.left.right
                    self._insert_tree(temp_tree)
                else:
                    # Leaf node deletion
                    self.root_node.left = None
                    return
            else:
                # Recurse down until match
                return self._delete(self.root_node.left, key)

        else: # key > self.node_root.key
            if key == self.root_node.right.key:
                if self.root_node.right.has_only_left():
                    self.root_node.right = self.root_node.right.left
                elif self.root_node.right.has_only_right():
                    self.root_node.right = self.root_node.right.right
                elif self.root_node.right.has_two_childen():
                    temp_tree = self.root_node.right.left
                    self.root_node.right = self.root_node.right.right
                    self._insert_tree(temp_tree)
                else:
                    # Leaf node deletion
                    self.root_node.right = None
                    return
            else:
                # Recurse down until match
                return self._delete(self.root_node.right, key)

    def _insert_tree(self, node):
        if node == None:
            return
        self.insert(node.key, node.value)
        self._insert_tree(node.left)
        self._insert_tree(node.right)
