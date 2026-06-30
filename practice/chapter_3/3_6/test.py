import unittest
import time
from datetime import datetime
from animal_shelter import Animal, Adoption_queue


class TestAnimalShelter(unittest.TestCase):

    def setUp(self):
        """Set up a fresh queue before every test."""
        self.queue = Adoption_queue()

    def test_enqueue_and_peek(self):
        """Test that animals are correctly enqueued and peek returns the head."""
        dog = Animal("dog")
        cat = Animal("cat")

        self.queue.enqueue(dog)
        self.queue.enqueue(cat)

        self.assertEqual(self.queue.peekDog(), dog)
        self.assertEqual(self.queue.peekCat(), cat)

    def test_enqueue_invalid_type(self):
        """Test that an invalid animal type raises an AttributeError."""
        rabbit = Animal("rabbit")
        with self.assertRaises(AttributeError):
            self.queue.enqueue(rabbit)

    def test_dequeue_dog_fifo(self):
        """Test that dogs are dequeued in strict First-In, First-Out order."""
        dog1 = Animal("dog")
        time.sleep(0.001)  # Ensure distinct timestamp
        dog2 = Animal("dog")

        self.queue.enqueue(dog1)
        self.queue.enqueue(dog2)

        self.assertEqual(self.queue.dequeueDog(), dog1)
        self.assertEqual(self.queue.dequeueDog(), dog2)

        # Queue should now be empty for dogs
        with self.assertRaises(EOFError):
            self.queue.dequeueDog()

    def test_dequeue_cat_fifo(self):
        """Test that cats are dequeued in strict First-In, First-Out order."""
        cat1 = Animal("cat")
        time.sleep(0.001)
        cat2 = Animal("cat")

        self.queue.enqueue(cat1)
        self.queue.enqueue(cat2)

        self.assertEqual(self.queue.dequeueCat(), cat1)
        self.assertEqual(self.queue.dequeueCat(), cat2)

        # Queue should now be empty for cats
        with self.assertRaises(EOFError):
            self.queue.dequeueCat()

    def test_dequeue_any_timestamp_comparison(self):
        """Test that dequeueAny pulls the older animal regardless of type."""
        dog = Animal("dog")
        time.sleep(0.001)
        cat = Animal("cat")

        self.queue.enqueue(dog)
        self.queue.enqueue(cat)

        # Dog arrived first, so dequeueAny must return the dog
        self.assertEqual(self.queue.dequeueAny(), dog)
        # Next should be the cat
        self.assertEqual(self.queue.dequeueAny(), cat)

    def test_dequeue_any_with_empty_sublists(self):
        """Test that dequeueAny works perfectly when only one animal type exists."""
        dog1 = Animal("dog")
        dog2 = Animal("dog")
        self.queue.enqueue(dog1)
        self.queue.enqueue(dog2)

        self.assertEqual(self.queue.dequeueAny(), dog1)
        self.assertEqual(self.queue.dequeueAny(), dog2)

        with self.assertRaises(EOFError):
            self.queue.dequeueAny()

    def test_empty_queue_exceptions(self):
        """Test that all peek and dequeue operations raise EOFError on empty queues."""
        with self.assertRaises(EOFError):
            self.queue.peekDog()
        with self.assertRaises(EOFError):
            self.queue.peekCat()
        with self.assertRaises(EOFError):
            self.queue.dequeueAny()
        with self.assertRaises(EOFError):
            self.queue.dequeueDog()
        with self.assertRaises(EOFError):
            self.queue.dequeueCat()


if __name__ == "__main__":
    unittest.main()
