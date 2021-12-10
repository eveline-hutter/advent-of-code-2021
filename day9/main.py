import copy
import math

with open('input9.txt') as file:
    puzzle_input = [[int(value) for value in line] for line in file.read().splitlines()]    # open without /n


def is_low_point(i, j):
    value = puzzle_input[i][j]
    # check top
    if i > 0:
        top = puzzle_input[i - 1][j]
        if top <= value: return False
    # check bottom
    if i < len(puzzle_input) - 1:
        bottom = puzzle_input[i + 1][j]
        if bottom <= value: return False
    # check left
    if j > 0:
        left = puzzle_input[i][j - 1]
        if left <= value: return False
    # check right
    if j < len(puzzle_input[i]) - 1:
        right = puzzle_input[i][j + 1]
        if right <= value: return False
    return True


def puzzle1():
    lowpoints = []
    for i in range(len(puzzle_input)):
        for j in range(len(puzzle_input[i])):
            value = puzzle_input[i][j]
            if is_low_point(i, j): lowpoints.append(value + 1)
    print('sum of risk levels of low points:', sum(lowpoints))


def puzzle2():
    def get_next_low_points(low_point, heightmap):
        x, y = low_point[0], low_point[1]
        next_low_points = []
        top, bottom, left, right = 9, 9, 9, 9
        # check top
        if x > 0:
            top = heightmap[x - 1][y]
        # check bottom
        if x < len(heightmap) - 1:
            bottom = heightmap[x + 1][y]
        # check left
        if y > 0:
            left = heightmap[x][y - 1]
        # check right
        if y < len(heightmap[x]) - 1:
            right = heightmap[x][y + 1]
        if min([top, bottom, left, right]) == 9: return []
        else:
            if top < 9: next_low_points.append([x - 1, y])
            if bottom < 9: next_low_points.append([x + 1, y])
            if left < 9: next_low_points.append([x, y - 1])
            if right < 9: next_low_points.append([x, y + 1])
            return next_low_points

    def identify_basin_size(low_point, heightmap):
        next_low_points = get_next_low_points(low_point, heightmap)
        basin_size = 1
        if (len(next_low_points)) == 0:
            return 1
        else:
            for next_point in next_low_points:
                x, y = next_point[0], next_point[1]
                if heightmap[x][y] != 9:
                    heightmap[x][y] = 9
                    basin_size += identify_basin_size(next_point, heightmap)
            return basin_size

    low_points = []
    for i in range(len(puzzle_input)):
        for j in range(len(puzzle_input[i])):
            if is_low_point(i, j): low_points.append([i, j])
    basins = []
    for low_point in low_points:
        heightmap = copy.deepcopy(puzzle_input)
        heightmap[low_point[0]][low_point[1]] = 9
        basins.append(identify_basin_size(low_point, heightmap))
    largest_basins = sorted(basins)[-3:]
    print('size of three largest basins:', math.prod(largest_basins))   # multiply three largest basins


puzzle1()
puzzle2()
