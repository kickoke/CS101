from string_rotation import isSubstring, isSubstring_efficient

original = "waterbottle"
rotation = "erbottlewat"
no_rotation = "botwatertle"


def test_no_rotation():
    assert isSubstring(original, original) == True
    assert isSubstring_efficient(original, original) == True


def test_valid_rotation():
    assert isSubstring(original, rotation) == True
    assert isSubstring_efficient(original, rotation) == True


def test_invalid_rotation():
    assert isSubstring(original, no_rotation) == False
    assert isSubstring_efficient(original, no_rotation) == False


def test_edge_cases():
    assert isSubstring("", "") == False
    assert isSubstring(original, "abc") == False
    assert isSubstring_efficient("", "") == False
    assert isSubstring_efficient(original, "abc") == False
