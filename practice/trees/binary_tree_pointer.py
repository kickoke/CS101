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

    def _delete(self, node, key):
        """Delete root node"""
        if key == node.key:
            old_root = node
            self.root_node = None
            self._insert_tree(old_root.left)
            self._insert_tree(old_root.right)

        """Delete node with one child (left)"""
        if key < node.key:
            if key == node.left.key:
                if node.left.has_only_left():
                    node.left = node.left.left
                elif node.left.has_only_right():
                    node.left = node.left.right
                elif node.left.has_two_childen():
                    temp_tree = node.left.left
                    node.left = node.left.right
                    self._insert_tree(temp_tree)
                else:
                    # Leaf node deletion
                    node.left = None
                    return
            else:
                # Recurse down until match
                return self._delete(node.left, key)

        else:  # key > self.node_root.key
            if key == node.right.key:
                if node.right.has_only_left():
                    node.right = node.right.left
                elif node.right.has_only_right():
                    node.right = node.right.right
                elif node.right.has_two_childen():
                    temp_tree = node.right.left
                    node.right = node.right.right
                    self._insert_tree(temp_tree)
                else:
                    # Leaf node deletion
                    node.right = None
                    return
            else:
                # Recurse down until match
                return self._delete(node.right, key)

    def delete(self, key):
        """Check empty tree"""
        if self.root_node == None:
            raise KeyError("No entries in tree.")
        return self._delete(self.root_node, key)

    def _insert_tree(self, node):
        if node == None:
            return
        self.insert(node.key, node.value)
        self._insert_tree(node.left)
        self._insert_tree(node.right)
