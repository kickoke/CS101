from urlify import urlify


def test_string():
    assert urlify("Mr John Smith   ") == "Mr%20John%20Smith"
    assert urlify("womens shoes fall") == "womens%20shoes%20fall"


def test_number():
    assert urlify(13) == None
