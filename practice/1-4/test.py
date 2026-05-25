from palindrome import is_palindrome


def test_palindrome():
    symmetric = "toot"  # otto
    asymmetric = "tact coa"  # taco cat
    base_case = "e"

    assert is_palindrome(symmetric) == True
    assert is_palindrome(asymmetric) == True
    assert is_palindrome(base_case) == True


def test_no_palindrome():
    not_p = "nope"
    assert is_palindrome(not_p) == False
