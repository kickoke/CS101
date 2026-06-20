from min_stack import Min_stack

import pytest


def test_empty_stack():
    s = Min_stack()
    assert s.peek() is None
    assert s.min() is None


def test_single_push():
    s = Min_stack()
    s.push(5)
    assert s.peek() == 5
    assert s.min() == 5


def test_increasing_values():
    s = Min_stack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.min() == 1


def test_decreasing_values():
    s = Min_stack()
    s.push(3)
    s.push(2)
    s.push(1)
    assert s.min() == 1


def test_pop_non_minimum():
    s = Min_stack()
    s.push(5)
    s.push(3)
    s.push(7)
    s.pop()
    assert s.min() == 3


def test_pop_minimum():
    s = Min_stack()
    s.push(5)
    s.push(3)
    s.push(7)
    s.pop()
    s.pop()
    assert s.min() == 5


def test_duplicate_minimums():
    s = Min_stack()
    s.push(5)
    s.push(2)
    s.push(2)
    s.push(3)

    assert s.min() == 2

    s.pop()  # 3
    s.pop()  # first 2
    assert s.min() == 2

    s.pop()  # second 2
    assert s.min() == 5


def test_negative_values():
    s = Min_stack()
    s.push(-1)
    s.push(-5)
    s.push(0)
    assert s.min() == -5


def test_pop_last_element():
    s = Min_stack()
    s.push(5)
    s.pop()
    assert s.peek() is None
    assert s.min() is None


def test_pop_empty_stack_raises():
    s = Min_stack()
    assert s.pop() is None
