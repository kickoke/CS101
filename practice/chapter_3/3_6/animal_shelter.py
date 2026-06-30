"""
An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first
out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
that type). They cannot select which specific animal they would like. Create the data structures to
maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
and dequeueCat. You may use the built-in LinkedList data structure.

"""

from datetime import datetime


class Animal:
    def __init__(self, animal):
        self.type = animal
        self.arrival = datetime.now()
        self.next = None


class Adoption_queue:
    def __init__(self):
        self.dogs_head = None
        self.dogs_tail = None
        self.cats_head = None
        self.cats_tail = None

    def enqueue(self, animal: Animal) -> None:
        # Enqueue at the end (tail)
        if animal.type == "dog":
            # Initialize with first animal
            if not self.dogs_head and not self.dogs_tail:
                self.dogs_head = animal
                self.dogs_tail = animal
            else:
                self.dogs_tail.next = animal
                self.dogs_tail = self.dogs_tail.next

        elif animal.type == "cat":
            if not self.cats_head and not self.cats_tail:
                self.cats_head = animal
                self.cats_tail = animal
            else:
                self.cats_tail.next = animal
                self.cats_tail = self.cats_tail.next
        else:
            raise AttributeError("Animal must be dog or a cat.")

    def peekDog(self):
        if self.dogs_head is None:
            raise EOFError("No dogs available to adopt.")
        return self.dogs_head

    def peekCat(self):
        if self.cats_head is None:
            raise EOFError("No cats available to adopt.")
        return self.cats_head

    def dequeueAny(self):
        # Dequeue from front (head)
        if self.dogs_head is None and self.cats_head is None:
            raise EOFError("No animals available to adopt.")
        if not self.dogs_head:
            return self.dequeueCat()
        if not self.cats_head:
            return self.dequeueDog()
        if self.dogs_head.arrival < self.cats_head.arrival:
            return self.dequeueDog()
        else:
            return self.dequeueCat()

    def dequeueDog(self):
        if self.dogs_head is None:
            raise EOFError("No dogs available to adopt.")

        dog = self.dogs_head
        # If last dog in queue, reset values to None
        if self.dogs_head == self.dogs_tail:
            self.dogs_head = None
            self.dogs_tail = None

        else:
            self.dogs_head = self.dogs_head.next
        return dog

    def dequeueCat(self):
        if self.cats_head is None:
            raise EOFError("No cats available to adopt.")
        cat = self.cats_head
        # If last cat in queue, reset values to None
        if self.cats_head == self.cats_tail:
            self.cats_tail = None
            self.cats_head = None
        else:
            self.cats_head = self.cats_head.next
        return cat
