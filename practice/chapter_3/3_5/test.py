from sort_stack import Stack, sort_stack

import unittest


class TestSortStack(unittest.TestCase):
    def test_sort_stack(self):
        stack = Stack()
        for value in [9, 5, 8, 2, 7]:
            stack.push(value)

        sorted_stack = sort_stack(stack)

        result = []
        while not sorted_stack.isEmpty():
            result.append(sorted_stack.pop())

        self.assertEqual(result, [2, 5, 7, 8, 9])

    def test_empty_stack(self):
        stack = Stack()

        sorted_stack = sort_stack(stack)

        self.assertTrue(sorted_stack.isEmpty())

    def test_single_element_stack(self):
        stack = Stack()
        stack.push(42)

        sorted_stack = sort_stack(stack)

        self.assertEqual(sorted_stack.pop(), 42)
        self.assertTrue(sorted_stack.isEmpty())


if __name__ == "__main__":
    unittest.main()
