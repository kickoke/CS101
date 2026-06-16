from partition import partition, Node
import unittest


class TestPartitionLinkedList(unittest.TestCase):

    def helper_to_list(self, head):
        """Helper function to convert linked list to a Python list for easy assertion."""
        result = []
        curr = head
        # Added a safety counter to prevent infinite loops if code has bugs
        visited = set() 
        while curr:
            if curr in visited:
                raise Exception("Cycle detected in linked list!")
            visited.add(curr)
            result.append(curr.data)
            curr = curr.next
        return result

    def helper_create_linked_list(self, arr):
        """Helper function to create a linked list from a Python list."""
        if not arr:
            return None
        head = Node(arr[0])
        curr = head
        for val in arr[1:]:
            curr.next = Node(val)
            curr = curr.next
        return head

    def test_empty_list(self):
        """Edge Case: The list is empty."""
        head = self.helper_create_linked_list([])
        new_head = partition(head, 5)
        self.assertIsNull = self.helper_to_list(new_head)
        self.assertEqual(self.helper_to_list(new_head), [])

    def test_single_element_less(self):
        """Edge Case: Single element less than x."""
        head = self.helper_create_linked_list([3])
        new_head = partition(head, 5)
        self.assertEqual(self.helper_to_list(new_head), [3])

    def test_single_element_greater(self):
        """Edge Case: Single element greater than x."""
        head = self.helper_create_linked_list([7])
        new_head = partition(head, 5)
        self.assertEqual(self.helper_to_list(new_head), [7])

    def test_all_elements_less_than_x(self):
        """Standard Case: All elements are strictly less than x."""
        head = self.helper_create_linked_list([1, 2, 3])
        new_head = partition(head, 5)
        # Note: Your implementation reverses the insertion order because of how it prepends
        self.assertEqual(self.helper_to_list(new_head), [3, 2, 1])

    def test_all_elements_greater_or_equal_to_x(self):
        """Standard Case: All elements are greater than or equal to x."""
        head = self.helper_create_linked_list([6, 7, 5])
        new_head = partition(head, 5)
        self.assertEqual(self.helper_to_list(new_head), [5, 7, 6])

    def test_mixed_elements(self):
        """Standard Case: General mix of elements less than, equal to, and greater than x."""
        head = self.helper_create_linked_list([3, 5, 8, 5, 10, 2, 1])
        # x = 5
        # Expected 'less than' group elements: 3, 2, 1 (will be reversed to 1, 2, 3)
        # Expected 'greater/equal' group elements: 5, 8, 5, 10 (will be reversed to 10, 5, 8, 5)
        new_head = partition(head, 5)
        self.assertEqual(self.helper_to_list(new_head), [1, 2, 3, 10, 5, 8, 5])

    def test_elements_equal_to_x(self):
        """Edge Case: Multiple elements exactly equal to x."""
        head = self.helper_create_linked_list([5, 5, 5])
        new_head = partition(head, 5)
        self.assertEqual(self.helper_to_list(new_head), [5, 5, 5])

if __name__ == '__main__':
    unittest.main()