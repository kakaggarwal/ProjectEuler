#!/bin/python3

import sys


def euler(grid):
		workGrid = [[0] * 3] * 23

		for i in range(23):
			workGrid[i] = workGrid[i] + grid[i] + [0] * 3

			if i > 19:
				workGrid[i] = workGrid[i] + [0] * 23

    res = 0

    for i in range(23):
        for j in range(3, 26):
            prod1 = grid[i][j] * grid[i][j + 1] * grid[i][j + 2] * grid[i][j + 3]

            prod2 = grid[i][j] * grid[i + 1][j + 1] * grid[i + 2][j + 2] * grid[i + 3][j + 3]

            prod3 = grid[i][j] * grid[i + 1][j] * grid[i + 2][j] * grid[i + 3][j]
            
						prod4 = grid[i][j] * grid[i + 1][j - 1] * grid[i + 2][j - 2] * grid[i + 3][j - 3]

						res = max(res, prod1, prod2, prod3, prod4)

    return res


grid = []

for grid_i in range(20):
    grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
    grid.append(grid_t)

    print(euler(grid))
