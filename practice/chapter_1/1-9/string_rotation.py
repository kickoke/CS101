"""
String rotation: Assume you have a method isSubstring which checks if one
word is a substring of another. Given two strings s1 and s2, check if s2 is a rotation of s1.

A rotation is when a string was cut off at a certain point and the left part was appended to the right.

Base case:
If lengths differ, it cannot be a rotation.

split s1 into two halves --> save to a set of strs to compute all possible solutions for s1
Check if s2 is in set for s1.
"""


def isSubstring(s1: str, s2: str) -> bool:
    """
    Space complexity = N^2
    Time complexity = N^2
    """

    # Case: Empty strings or different lengths
    if len(s1) == 0 or len(s2) == 0 or len(s1) != len(s2):
        return False
    # Lucky case: no rotations
    if s1 == s2:
        return True

    string_rotations = set()
    # Build set of string rotations:
    for i in range(len(s1)):
        x = s1[:i]
        y = s1[i:]
        rotation = y + x
        string_rotations.add(rotation)

    if s2 in string_rotations:
        return True

    return False


def isSubstring_efficient(s1: str, s2: str) -> bool:
    """
    Space complexity: O(2n) --> O(n)
    Time complexity: O(n)
    """
    # Case: Empty strings or different lengths
    if len(s1) == 0 or len(s2) == 0 or len(s1) != len(s2):
        return False
    # Lucky case: no rotations
    if s1 == s2:
        return True
    concat = s2 + s2
    if s1 in concat:
        return True
    return False
