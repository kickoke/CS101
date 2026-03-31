"""
Practice Question 1.1

How to check if a string has only unique values?

Approach:
1. Sort string (Merge sort)
2. Check if two neighboring values are the same
"""

to_sort_unique = "asdfghjklzxcvbnm"
to_sort_not_unique = "asdfghjklzxcvghjki"

def mergesort(to_sort: str)-> list:
    to_sort_chars = list(to_sort)
    # Base case: Only 1 character
    if len(to_sort_chars) == 1:
        sorted = to_sort_chars
        return sorted
    
    # Split into half
    halfway_point = int(len(to_sort)/2)
    to_sort_left = to_sort_chars[:halfway_point]
    to_sort_right = to_sort_chars[halfway_point:]

    left = mergesort(to_sort_left)
    right = mergesort(to_sort_right)
    sorted = merge(left, right)
    return sorted

def merge(left: list, right: list) -> list:
    sorted =[]
    while len(left) != 0 and len(right) != 0:
        if left[0]>right[0]:
            sorted.append(right[0])
            right.pop(0)
        else:
            sorted.append(left[0])
            left.pop(0)
    # Deal with remaining elements
    while left:
        sorted.append(left[0])
        left.pop(0)

    while right:
        sorted.append(right[0])
        right.pop(0)

    return sorted

def is_unique(sorted):
    for i in range(0, (len(sorted)-1)):
        if sorted[i] == sorted[i+1]:
            return False
    return True


sorted_unique = mergesort(to_sort_unique)

print(sorted_unique)
print(is_unique(sorted_unique))

sorted_not_unique = mergesort(to_sort_not_unique)
print(sorted_not_unique)
print(is_unique(sorted_not_unique))
