"""
Implement a data structure (`Set_of_Stacks`) that mimics a stack of plates.
When the stack gets too high, start another one.
Set_of_Stacks.push() and Set_of_Stacks.pop() should behave identically to
a single stack. That is pop() should return the same values as if it were
just a single stack.


Follow-up: Implement a popAt(index) function which performs a pop on a specific sub-stack
---
Assuming that we will use a Python list for a single stack, we can use a
list of lists for the Set of Stacks.

To construct this, we need to know when the user would like to start a
new stack -> max_length

When the set of stacks is empty, return none.
"""


class Set_of_Stacks:
    def __init__(self, max_length=10):
        self.set_of_stacks = []
        self.max_length = max_length
        self.current_stack = 0

    def _update_current_stack(self):
        self.current_stack = len(self.set_of_stacks) - 1

    def push(self, item):
        if (
            len(self.set_of_stacks) == 0
            or len(self.set_of_stacks[self.current_stack]) == self.max_length
        ):
            self.set_of_stacks.append([item])
        else:
            self.set_of_stacks[self.current_stack].append(item)
        self._update_current_stack()

    def pop(self):
        # Base case: Empty set of stacks
        if len(self.set_of_stacks) == 0:
            return None
        value = self.set_of_stacks[self.current_stack].pop()
        # Cleanup if we were left with an empty list.
        if len(self.set_of_stacks[self.current_stack]) == 0:
            self.set_of_stacks.pop()
            if not len(self.set_of_stacks) == 0:
                self._update_current_stack()
        return value

    def peek(self):
        if len(self.set_of_stacks) == 0:
            return None
        return self.set_of_stacks[self.current_stack][-1]
