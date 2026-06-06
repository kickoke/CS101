from edits import edit_distance

def test_correct():
    assert edit_distance("pales", "pale") == True
    assert edit_distance("pale", "bale") == True
    assert edit_distance("pale", "pales") == True

def test_longer_than_1():
    assert edit_distance("abracadabra", "abra") == False
    assert edit_distance("abracadabra", "abracadabracadabra") == False
    assert edit_distance("abracadabra", "jbracjdjbrj") == False