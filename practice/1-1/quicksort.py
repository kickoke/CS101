"""
Practice Question 1.1

How to check if a string has only unique values?

Approach:
1. Sort string (Merge sort)
2. Check if two neighboring values are the same
"""

to_sort_unique = "asdfghjklzxcvbnm"
to_sort_not_unique = "asdfghjklzxcvghjki"

def quicksort(to_sort: str) -> list:
  # Base case: already sorted
  if len(to_sort) == 1:
    to_sort = sorted
    return sorted
  
  pivot_index = int(len(to_sort)/2)
  pivot_value = to_sort[pivot_index]
  to_sort_left = to_sort[:pivot_index]
  to_sort_right = to_sort[pivot_index+1:]
  left =[]
  right =[]

  while to_sort_left:
    if 


def is_unique(sorted):
    for i in range(0, (len(sorted)-1)):
        if sorted[i] == sorted[i+1]:
            return False
    return True


sorted_unique = quicksort(to_sort_unique)

print(sorted_unique)
print(is_unique(sorted_unique))

sorted_not_unique = quicksort(to_sort_not_unique)
print(sorted_not_unique)
print(is_unique(sorted_not_unique))
