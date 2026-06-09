from delete_middle import delete, Node

import unittest


class TestDeleteMiddleNode(unittest.TestCase):

    def helper_create_list(self, values):
        """Helper method to create a linked list from a list of values."""
        if not values:
            return None
        head = Node(values[0])
        current = head
        for val in values[1:]:
            current.next = Node(val)
            current = current.next
        return head

    def helper_to_list(self, head):
        """Helper method to convert a linked list back to a Python list."""
        result = []
        current = head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def test_delete_exact_middle_node(self):
        """Test deleting a node exactly in the middle of an odd-length list."""
        # List: 1 -> 2 -> 3 -> 4 -> 5
        head = self.helper_create_list([1, 2, 3, 4, 5])
        node_to_delete = head.next.next  # Node with data 3
        
        delete(node_to_delete)
        
        self.assertEqual(self.helper_to_list(head), [1, 2, 4, 5])

    def test_delete_second_node_of_three(self):
        """Test deleting the middle node of a minimal 3-node list."""
        # List: 10 -> 20 -> 30
        head = self.helper_create_list([10, 20, 30])
        node_to_delete = head.next  # Node with data 20
        
        delete(node_to_delete)
        
        self.assertEqual(self.helper_to_list(head), [10, 30])

    def test_delete_head_node_as_middle(self):
        """Test deleting the head node when it is technically followed by other nodes."""
        # List: A -> B -> C -> D
        head = self.helper_create_list(['A', 'B', 'C', 'D'])
        
        # Deleting the head node works with this algorithm because it has a next node
        delete(head)
        
        self.assertEqual(self.helper_to_list(head), ['B', 'C', 'D'])

    def test_delete_last_node_raises_exception(self):
        """Test that attempting to delete the very last node raises an Exception."""
        # List: 1 -> 2 -> 3
        head = self.helper_create_list([1, 2, 3])
        last_node = head.next.next  # Node with data 3
        
        with self.assertRaises(Exception) as context:
            delete(last_node)
        
        self.assertIn("Can't delete since not a middle node", str(context.exception))

    def test_delete_single_node_list_raises_exception(self):
        """Test that a list with only one node raises an Exception because it has no 'next'."""
        head = Node(42)
        
        with self.assertRaises(Exception) as context:
            delete(head)
            
        self.assertIn("Can't delete since not a middle node", str(context.exception))

    def test_delete_none_node_raises_exception(self):
        """Test passing None to the delete function raises an Exception."""
        with self.assertRaises(Exception) as context:
            delete(None)
            
        self.assertIn("Can't delete since not a middle node", str(context.exception))

if __name__ == '__main__':
    unittest.main()