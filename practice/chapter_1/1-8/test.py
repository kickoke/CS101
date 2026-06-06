from zero_matrix import matrix_zerofy

no_zeros = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
one_zero = [[1, 1, 1], [1, 1, 1], [1, 1, 0], [1, 1, 1]]
two_zeros = [[1, 0, 1], [1, 1, 1], [1, 1, 0], [1, 1, 1]]

one_zero_expected = [[1, 1, 0], [1, 1, 0], [0, 0, 0], [1, 1, 0]]
two_zeros_expected = [[0, 0, 0], [1, 0, 0], [0, 0, 0], [1, 0, 0]]


def test_no_zeros():
    assert matrix_zerofy(no_zeros) == no_zeros


def test_one_zero():
    assert matrix_zerofy(one_zero) == one_zero_expected


def test_two_zeros():
    assert matrix_zerofy(two_zeros) == two_zeros_expected
