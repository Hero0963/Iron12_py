from typing import List


class Solution1:
    """
    solution 1
    runtime=O(N), N=mn
    space=O(1)

    """

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count = 0
        lx = len(grid)
        ly = len(grid[0])

        for i in range(lx):
            for j in range(ly):

                # in water region
                if grid[i][j] == 0:
                    continue

                # up
                if j - 1 < 0 or grid[i][j - 1] == 0:
                    count += 1

                # down
                if j + 1 >= ly or grid[i][j + 1] == 0:
                    count += 1

                # left
                if i - 1 < 0 or grid[i - 1][j] == 0:
                    count += 1

                # right
                if i + 1 >= lx or grid[i + 1][j] == 0:
                    count += 1

        return count


class Solution2:
    """
    solution 2
    runtime=O(N), N=mn
    space=O(1)
    """

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):

                # in water region
                if grid[i][j] == 0:
                    continue

                # up
                if j - 1 < 0 or grid[i][j - 1] == 0:
                    perimeter += 1

                # down
                if j + 1 >= cols or grid[i][j + 1] == 0:
                    perimeter += 1

                # left
                if i - 1 < 0 or grid[i - 1][j] == 0:
                    perimeter += 1

                # right
                if i + 1 >= rows or grid[i + 1][j] == 0:
                    perimeter += 1

        return perimeter
