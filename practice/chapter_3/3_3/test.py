import pytest

from plates import Set_of_Stacks


def test_push_single_item():
    stacks = Set_of_Stacks()

    stacks.push(1)

    assert stacks.set_of_stacks == [[1]]
    assert stacks.current_stack == 0


def test_push_until_max_length():
    stacks = Set_of_Stacks(max_length=3)

    stacks.push(1)
    stacks.push(2)
    stacks.push(3)

    assert stacks.set_of_stacks == [[1, 2, 3]]
    assert stacks.current_stack == 0


def test_push_creates_new_stack_when_full():
    stacks = Set_of_Stacks(max_length=3)

    for i in range(1, 5):
        stacks.push(i)

    assert stacks.set_of_stacks == [
        [1, 2, 3],
        [4],
    ]
    assert stacks.current_stack == 1


def test_peek_returns_top_item():
    stacks = Set_of_Stacks()

    stacks.push("a")
    stacks.push("b")

    assert stacks.peek() == "b"


def test_peek_on_empty_returns_none():
    stacks = Set_of_Stacks()

    assert stacks.peek() is None


def test_pop_returns_last_item():
    stacks = Set_of_Stacks()

    stacks.push(1)
    stacks.push(2)

    assert stacks.pop() == 2
    assert stacks.peek() == 1


def test_pop_on_empty_returns_none():
    stacks = Set_of_Stacks()

    assert stacks.pop() is None


def test_pop_removes_empty_substack():
    stacks = Set_of_Stacks(max_length=2)

    stacks.push(1)
    stacks.push(2)
    stacks.push(3)

    assert stacks.set_of_stacks == [[1, 2], [3]]

    assert stacks.pop() == 3

    assert stacks.set_of_stacks == [[1, 2]]
    assert stacks.current_stack == 0


def test_lifo_behavior_across_multiple_stacks():
    stacks = Set_of_Stacks(max_length=2)

    for i in range(1, 6):
        stacks.push(i)

    popped = [stacks.pop() for _ in range(5)]

    assert popped == [5, 4, 3, 2, 1]
