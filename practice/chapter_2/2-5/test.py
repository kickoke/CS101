import unittest
from sum_list import Node, sum_lists

class TestSumLinkedLists(unittest.TestCase):
    
    def helper_to_linked_list(self, lst):
        """Helper to convert a Python list to a Linked List."""
        if not lst:
            return None
        head = Node(lst[0])
        current = head
        for val in lst[1:]:
            current.next = Node(val)
            current = current.next
        return head

    def helper_to_python_list(self, head):
        """Helper to convert a Linked List back to a Python list for easy assertion."""
        lst = []
        current = head
        while current:
            lst.append(current.data)
            current = current.next
        return lst

    def test_equal_length_with_carryover(self):
        # 342 + 465 = 807
        # Input lists represent digits in reverse order: [2 -> 4 -> 3] and [5 -> 6 -> 4]
        x = self.helper_to_linked_list([2, 4, 3])
        y = self.helper_to_linked_list([5, 6, 4])
        
        result = sum_lists(x, y)
        self.assertEqual(self.helper_to_python_list(result), [7, 0, 8])

    def test_different_lengths(self):
        # 99 + 1 = 100
        # [9 -> 9] + [1] = [0 -> 0 -> 1]
        x = self.helper_to_linked_list([9, 9])
        y = self.helper_to_linked_list([1])
        
        result = sum_lists(x, y)
        self.assertEqual(self.helper_to_python_list(result), [0, 0, 1])

    def test_final_carryover_creates_new_node(self):
        # 5 + 5 = 10
        # [5] + [5] = [0 -> 1]
        x = self.helper_to_linked_list([5])
        y = self.helper_to_linked_list([5])
        
        result = sum_lists(x, y)
        self.assertEqual(self.helper_to_python_list(result), [0, 1])

if __name__ == '__main__':
    unittest.main()