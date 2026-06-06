"""
Given an image represented by an N x N matrix, where each pixel is 4 bytes,
write a method to rotate the image by 90 degrees.
Can you do this in place?

---
What exactly does my input look like?

I am assuming this:
image = [[(pixel), (pixel), (pixel)],
        [(pixel), (pixel), (pixel)],
        [(pixel), (pixel), (pixel)]]

90 degree rotation means that one row becomes one column.
Assuming that we rotate around [0][0], this means:

The 0th row becomes the 0th column, like this:

orig: [0][0] [0][1] [0][2]

rotated: [0][0] [1][0] [2][0]

for 1st second row, we do the same

orig: [1][0] [1][1] [1][2]
rotated: [0][1]
"""


def rotate(grid: list) -> list:
    """
    Rotates in one step by clever looping
    """
    rotated_clockwise = []
    for i in range(0, len(grid)):
        current_row = []
        for j in range(len(grid) - 1, -1, -1):
            current_row.append(grid[j][i])
        rotated_clockwise.append(current_row)

    return rotated_clockwise


def rotate_in_place(grid: list) -> None:
    """Uses transpose & reverse"""
    for i in range(len(grid)):
        for j in range(i + 1, len(grid)):
            grid[i][j], grid[j][i] = grid[j][i], grid[i][j]
    for row in grid:
        row.reverse()
    return
