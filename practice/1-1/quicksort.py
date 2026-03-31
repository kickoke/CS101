"""
Practice Question 1.1

How to check if a string has only unique values?

Approach:
1. Sort string (Merge sort)
2. Check if two neighboring values are the same
"""

to_sort_unique = "asdfghjklzxcvbnm"
to_sort_not_unique = "asdfghjklzxcvghjki"

def quicksort(input: str) -> list:
  # Convert str into list
  to_sort = list(input)
  sorted = []
  # Base case: already sorted
  if len(to_sort) == 1:
    sorted = to_sort
    return sorted
  # Create pivot point and store value
  pivot_index = int(len(to_sort)/2)
  pivot_value = to_sort[pivot_index]
  # Split halves
  to_sort_left = to_sort[:pivot_index]
  to_sort_right = to_sort[pivot_index+1:]

  sorted_left = []
  sorted_right = []
  
  while to_sort_left:
    if to_sort_left[0] < pivot_value:
      sorted_left.append(to_sort_left[0])
      to_sort_left.pop(0)
    else:
      sorted_right.append(to_sort_left[0])
      to_sort_left.pop(0)
  
  while to_sort_right:
    if to_sort_right[0] < pivot_value:
      sorted_left.append(to_sort_right[0])
      to_sort_right.pop(0)
    else:
      sorted_right.append(to_sort_right[0])
      to_sort_right.pop(0)
    

  sorted = quicksort(sorted_left)+[pivot_value]+quicksort(sorted_right)
  return sorted
  

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
