"""
There are 3 types of edits that can be made to a string: add a char, remove a char, edit a char.
Write a function that determines if two strings are 1 edit away
---
edit --> len of both is the same
add --> len +1
remove --> len-1

Assuming that s1 is base and s2 is test side
"""

import numpy as np


def edit_distance(s1: str, s2: str) -> bool:
    # No edits case
    if s1 == s2:
        return True
    # Base case: more or less than 1 edit distance
    if not abs(len(s1)-len(s2)) == 1 and not len(s1)==len(s2):
        return False

    # First string is row
    rows = len(s1) + 1
    cols = len(s2) + 1
    # Create empty 2D array
    charmap = [[0] * cols for _ in range(rows)]

    # Populate with strings
    for i in range(1, rows):
        charmap[i][0] = i

    for j in range(1, cols):
        charmap[0][j] = j

    # Populate edit distance table
    for i in range(1, rows):
        for j in range(1, cols):
            if s1[i - 1] == s2[j - 1]:
                cost = 0
            else:
                cost = 1
            charmap[i][j] = min(
                charmap[i - 1][j] + 1,  # Deletion
                charmap[i][j - 1] + 1,  # Insertion
                charmap[i - 1][j - 1] + cost,  # Substitution
            )
    if charmap[-1][-1] > 2:
        return False
    else:
        return True
