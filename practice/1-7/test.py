from rotate_matrix import rotate, rotate_in_place
import unittest


class TestMatrixRotation(unittest.TestCase):

    def setUp(self):
        # Fresh test data before every test run
        self.grid_3x3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.expected_3x3 = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

        self.grid_4x4 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        self.expected_4x4 = [
            [13, 9, 5, 1],
            [14, 10, 6, 2],
            [15, 11, 7, 3],
            [16, 12, 8, 4],
        ]

    def test_rotate_out_of_place_3x3(self):
        # Tests that the out-of-place function works and leaves the original intact
        result = rotate(self.grid_3x3)
        self.assertEqual(result, self.expected_3x3)
        # Verify the original matrix didn't accidentally mutate
        self.assertNotEqual(self.grid_3x3, self.expected_3x3)

    def test_rotate_in_place_3x3(self):
        # Tests that the in-place function mutates the original grid correctly
        rotate_in_place(self.grid_3x3)
        self.assertEqual(self.grid_3x3, self.expected_3x3)

    def test_rotate_in_place_4x4(self):
        # Tests a larger even-numbered dimension matrix
        rotate_in_place(self.grid_4x4)
        self.assertEqual(self.grid_4x4, self.expected_4x4)

    def test_single_element_grid(self):
        # Edge case: A 1x1 matrix should remain unchanged
        grid_1x1 = [[42]]

        # Test out-of-place
        self.assertEqual(rotate(grid_1x1), [[42]])

        # Test in-place
        rotate_in_place(grid_1x1)
        self.assertEqual(grid_1x1, [[42]])


if __name__ == "__main__":
    unittest.main()
