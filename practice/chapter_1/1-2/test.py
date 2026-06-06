import string_permutations as sp

original = "CAT"
permutation = "ACT"
not_permutation = "BAT"


def test_permutation():
    assert sp.permutation(original, permutation) == True


def test_no_permutation():
    assert sp.permutation(original, not_permutation) == False
