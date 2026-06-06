"""
Practice Question 1.1

How to check if a string has only unique values?

Approach:
1. Sort string (quick sort)
2. Check if two neighboring values are the same
----
Quicksort steps:
1. Pick a pivot (index, value)
2. Move pivot to the end of the array
3. Use two pointers, one starting from the left and one starting to the right and compare values. Swap if right < left.
4. Linearly move through the array and do the swapping until the pointers have crossed over (index of right pointer is smaller than index of left pointer)
5. Re-place pivot at correct place by swapping with last index of "from left" pointer

# Important: This all happens in-place. No shadow copies of the partionioned arrays.
"""


def partition(array: list, low: int, high: int) -> int:
    """
    Partitioning scheme for quicksort:
    Picks pivot & reassembles values so that:
    * left of pivot is smaller
    * right of pivot is larger
    """
    # Base case 
    if len(array) == 1:
        return 0
    
    # Starting index of the left (low) scanner
    i = low
    # Pick pivot point in the middle of the array slice
    mid = (low+high)//2
    pivot = array[mid] # store a copy of the value for comparisons
    # Place pivot value at the end of the array
    array[mid], array[high] = array[high], array[mid]

    # Loop over the array slice and swap values
    # Note: Pivot is now at very end
    for j in range(low, high):
        # Compare and swap values
        if array[i] > pivot:
            if array[j] <= pivot:
                array[i], array[j] = array[j], array[i]
        if array[i] < pivot:
            i = i+1
    # Place pivot at its right place
    array[i], array[high] = array[high], array[i]
    return i
    
def quicksort(array: list, low: int, high: int)-> None:
    # Check if inputs make sense
    if low < high:
        # Divide array according to partition index & sort halves
        partition_index = partition(array, low, high)
        quicksort(array, low, partition_index-1)
        quicksort(array, partition_index+1, high)


def is_unique(sorted_array: list):
    for i in range(0, (len(sorted_array)-1)):
        if sorted_array[i] == sorted_array[i+1]:
            return False
    return True


def main():
    # Inputs
    to_sort_unique = "asdfghjklzxcvbnm"
    to_sort_not_unique = "asdfghjklzxcvghjki"

    # listify
    to_sort_unique = list(to_sort_unique)
    to_sort_not_unique = list(to_sort_not_unique)

    # Sort
    quicksort(to_sort_unique, 0, len(to_sort_unique)-1)
    print(to_sort_unique)
    print(is_unique(to_sort_unique))
    
    print(quicksort(to_sort_not_unique, 0, len(to_sort_not_unique)-1))
    print(to_sort_not_unique)
    print(is_unique(to_sort_not_unique))

main()