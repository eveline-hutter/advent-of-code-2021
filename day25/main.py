import copy
import numpy as np

with open('input25.txt') as file: puzzle_input = [list(line) for line in file.read().splitlines()]

seafloor = np.array(puzzle_input)
moving, steps = True, 0

while moving:
    moving = False
    steps += 1
    seafloor_copy = copy.deepcopy(seafloor)
    # move all east-facing cucumbers
    for i in range(len(seafloor)):
        for j in range(len(seafloor[i])):
            location = seafloor[i][j]
            if location == '>':
                neighbour_j = 0 if j == len(seafloor[i]) - 1 else j+1
                neighbouring_location = seafloor[i][neighbour_j]
                if neighbouring_location == '.':
                    seafloor_copy[i][j] = '.'
                    seafloor_copy[i][neighbour_j] = '>'
                    moving = True
    seafloor = seafloor_copy
    seafloor_copy = copy.deepcopy(seafloor)
    # move all south-facing cucumbers
    for i in range(len(seafloor)):
        for j in range(len(seafloor[i])):
            location = seafloor[i][j]
            if location == 'v':
                neighbour_i = 0 if i == len(seafloor) - 1 else i+1
                neighbouring_location = seafloor[neighbour_i][j]
                if neighbouring_location == '.':
                    seafloor_copy[i][j] = '.'
                    seafloor_copy[neighbour_i][j] = 'v'
                    moving = True
    seafloor = seafloor_copy

print('no of steps after which no cucumber moves', steps)
