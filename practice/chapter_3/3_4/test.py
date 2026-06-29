import unittest
from queue_stack import MyQueue


class TestMyQueue(unittest.TestCase):
    def test_enqueue_dequeue_and_peek(self):
        q = MyQueue()

        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)

        self.assertEqual(q.peek(), "No items in the queue")
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.peek(), 2)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)


if __name__ == "__main__":
    unittest.main()
