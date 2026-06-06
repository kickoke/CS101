"""
A string is a permutation of a string if it contains the same characters, in the same quantities, but in a different order.

Not permutations:
* If two strings have different lengths
* If they contain different characters

To simplify the problem, the strings will be normalized to lowercase and all whitespaces stripped.

one possible solution: Create a hash map of length of the alphabet
alternative solution: If the strings do indeed have the same length, I could just sort each string and do a linear comparison between the two.
"""


def permutation(base: str, test: str) -> bool:
    base = base.strip().lower()
    test = test.strip().lower()
    if not len(base) == len(test):
        return False

    base_map = {}
    test_map = {}

    for char in base:
        if char not in base_map.keys():
            base_map.update({char: 1})
        if char in base_map.keys():
            count = base_map.get(char) + 1
            base_map.update({char: count})

    for char in test:
        if char not in test_map.keys():
            test_map.update({char: 1})
        if char in test_map.keys():
            count = test_map.get(char) + 1
            test_map.update({char: count})

    if base_map == test_map:
        return True
    return False
