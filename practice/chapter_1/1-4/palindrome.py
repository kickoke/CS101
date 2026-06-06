"""
Given a string, write a function to check if the string is a palindrome of the other string.
Palindrome means a word (or sequence of words) can be read forwards and backwards
Permutation means rearrangement of letters.
Palindrome does not need to be restricted to dictionary words.
---
since I have to check a permutation:
palindrome has symmetric amount of chars:
1, 2, 4, 6, 8, 10, etc.
Can have only 1 char 1x
Rest have to be present at least 2 times
"""


def is_palindrome(s: str) -> bool:
    # Base case: 1 char can always be read forward and backward
    if len(s) == 1:
        return True
    # Get all chars from string
    chars = list(s.strip())
    char_frequency = dict()
    # Create a hashtable to count how many chars of each are present in the word
    for char in chars:
        if char == " ":
            continue
        elif char not in char_frequency.keys():
            char_frequency.update({char: 1})
        else:
            char_frequency[char] += 1

    unique_char = 0
    for val in char_frequency.values():
        if val == 1:
            unique_char = unique_char + 1
        elif val % 2 == 1 and val > 1:
            return False
        else:
            continue

    if unique_char > 1:
        return False

    else:
        return True
