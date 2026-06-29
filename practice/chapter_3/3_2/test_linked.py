import unittest
from min_stack_linked import Node, MinStack


class TestMinStack(unittest.TestCase):

    def test_new_stack_is_empty(self):
        stack = MinStack()
        self.assertEqual(stack.stackSize(), 0)
        self.assertEqual(stack.peek(), "Stack is empty")
        self.assertEqual(stack.StackMin(), "Stack is empty")

    def test_push_single_element(self):
        stack = MinStack()
        stack.push(5)

        self.assertEqual(stack.peek(), 5)
        self.assertEqual(stack.StackMin(), 5)
        self.assertEqual(stack.stackSize(), 1)

    def test_push_multiple_elements(self):
        stack = MinStack()
        stack.push(5)
        stack.push(3)
        stack.push(7)

        self.assertEqual(stack.peek(), 7)
        self.assertEqual(stack.StackMin(), 3)
        self.assertEqual(stack.stackSize(), 3)

    def test_min_updates_correctly(self):
        stack = MinStack()

        stack.push(5)
        self.assertEqual(stack.StackMin(), 5)

        stack.push(2)
        self.assertEqual(stack.StackMin(), 2)

        stack.push(8)
        self.assertEqual(stack.StackMin(), 2)

        stack.push(1)
        self.assertEqual(stack.StackMin(), 1)

    def test_pop_returns_last_element(self):
        stack = MinStack()

        stack.push(1)
        stack.push(2)
        stack.push(3)

        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.peek(), 2)
        self.assertEqual(stack.stackSize(), 2)

    def test_min_after_pop(self):
        stack = MinStack()

        stack.push(5)
        stack.push(2)
        stack.push(8)

        stack.pop()  # removes 8
        self.assertEqual(stack.StackMin(), 2)

        stack.pop()  # removes 2
        self.assertEqual(stack.StackMin(), 5)

    def test_duplicate_minimums(self):
        stack = MinStack()

        stack.push(4)
        stack.push(2)
        stack.push(2)
        stack.push(5)

        self.assertEqual(stack.StackMin(), 2)

        stack.pop()  # remove 5
        self.assertEqual(stack.StackMin(), 2)

        stack.pop()  # remove second 2
        self.assertEqual(stack.StackMin(), 2)

        stack.pop()  # remove first 2
        self.assertEqual(stack.StackMin(), 4)

    def test_negative_numbers(self):
        stack = MinStack()

        stack.push(3)
        stack.push(-1)
        stack.push(-5)
        stack.push(2)

        self.assertEqual(stack.StackMin(), -5)

        stack.pop()
        self.assertEqual(stack.StackMin(), -5)

        stack.pop()
        self.assertEqual(stack.StackMin(), -1)

    def test_pop_until_empty(self):
        stack = MinStack()

        stack.push(1)
        stack.push(2)

        stack.pop()
        stack.pop()

        self.assertEqual(stack.stackSize(), 0)
        self.assertEqual(stack.peek(), "Stack is empty")
        self.assertEqual(stack.StackMin(), "Stack is empty")
        self.assertEqual(stack.pop(), "Stack is empty")

    def test_size_updates_correctly(self):
        stack = MinStack()

        self.assertEqual(stack.stackSize(), 0)

        stack.push(1)
        self.assertEqual(stack.stackSize(), 1)

        stack.push(2)
        self.assertEqual(stack.stackSize(), 2)

        stack.pop()
        self.assertEqual(stack.stackSize(), 1)

        stack.pop()
        self.assertEqual(stack.stackSize(), 0)


if __name__ == "__main__":
    unittest.main()
