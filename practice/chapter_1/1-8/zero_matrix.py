"""
Write an algorithm such that if an element in an MxN matrix is 0,
its entire row **and** column are set to 0.
---
Steps:
* determine whether 0 present, if yes, save index.
  Since there could be multiple 0s in a row, we need
  to save all matches to make sure we can correctly
  nullify the columns.
* Nullify all values in row
* Nullify all values in column
* Return matrix

One way to know if a 0 is present is to multiply all values in a row and see if the checksum = 0.
For checksums > 0, we can skip a row.
However, that would likely involve touching each element in the row.
If we have to touch each value anyways, we can directly compare if == 0?
"""


def matrix_zerofy(grid: list) -> list:
    rows = len(grid)
    columns = len(grid[0])  # assuming no jagged matrix
    # Stores a list of tuples where grid[i][j] == 0.
    matches = []
    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == 0:
                matches.append((i, j))
            else:
                continue
    # If matrix has no 0, we can return early
    if len(matches) == 0:
        return grid

    for match in matches:
        # Unpack tuple for easy access to row and column.
        row = match[0]
        column = match[1]
        # nullify every cell in row
        for i, cell in enumerate(grid[row]):
            grid[row][i] = 0
        if rows == 1:  # Nullify column not necessary if only one row
            return grid
        # nullify column
        for i in range(rows):
            grid[i][column] = 0

    return grid
