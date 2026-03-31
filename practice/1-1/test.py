from mergesort import mergesort
from mergesort import is_unique
from quicksort import quicksort

to_sort_unique = "asdfghjklzxcvbnm"
to_sort_not_unique = "asdfghjklzxcvghjki"
sorted_unique = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 's', 'v', 'x', 'z']
sorted_not_unique = ['a', 'c', 'd', 'f', 'g', 'g', 'h', 'h', 'i', 'j', 'j', 'k', 'k', 'l', 's', 'v', 'x', 'z']

def test_is_unique():
    assert is_unique(sorted_unique) == True
    assert is_unique(sorted_unique) == False

def test_mergesort():
    assert mergesort(to_sort_unique) == sorted_unique
    assert mergesort(to_sort_not_unique) == sorted_not_unique

def test_quicksort():
    assert quicksort(to_sort_unique) == sorted_unique
    assert quicksort(to_sort_not_unique) == sorted_not_unique
