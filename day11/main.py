import copy
import numpy as np

with open('input11.txt') as file: puzzle_input = np.array([[int(value) for value in line] for line in file.read().splitlines()])    # open without /n


def model_energy_levels(energy_levels, flashed, no_of_flashes):
    max_energy = energy_levels > 9  # flag those octopi with max energy level
    flashing = max_energy ^ flashed  # only flash those octopi that were not yet flashed
    no_of_flashes += flashing.sum()  # how many octopi flashed?
    if flashing.sum() == 0:
        # set energy level of all flashing octopi to 0
        for i in range(len(flashed)):
            for j in range(len(flashed[0])):
                if flashed[i][j]: energy_levels[i][j] = 0
        return energy_levels, no_of_flashes
    else:
        flashed += flashing
        max_i, max_j = len(flashing) - 1, len(flashing[0]) - 1
        for i in range(len(flashing)):
            for j in range(len(flashing[0])):
                if flashing[i][j]:
                    # increase energy level of all surrounding octopi by 1
                    if i > 0 and j > 0 and not flashed[i - 1][j - 1]: energy_levels[i - 1][j - 1] += 1  # top left
                    if i > 0 and not flashed[i - 1][j]: energy_levels[i - 1][j] += 1  # top center
                    if i > 0 and j < max_j and not flashed[i - 1][j + 1]: energy_levels[i - 1][j + 1] += 1  # top right
                    if j > 0 and not flashed[i][j - 1]: energy_levels[i][j - 1] += 1  # center left
                    if j < max_j and not flashed[i][j + 1]: energy_levels[i][j + 1] += 1  # center right
                    if i < max_i and j > 0 and not flashed[i + 1][j - 1]: energy_levels[i + 1][
                        j - 1] += 1  # bottom left
                    if i < max_i and not flashed[i + 1][j]: energy_levels[i + 1][j] += 1  # bottom center
                    if i < max_i and j < max_j and not flashed[i + 1][j + 1]: energy_levels[i + 1][
                        j + 1] += 1  # bottom right
        return model_energy_levels(energy_levels, flashed, no_of_flashes)


def puzzle1():
    energy_levels = copy.deepcopy(puzzle_input)
    total_no_of_flashes = 0
    steps = 100
    for step in range(steps):
        energy_levels += 1  # increase energy level of each octopus
        flashed = np.array([[False for _ in line] for line in puzzle_input])
        infos_for_next_stop = model_energy_levels(energy_levels, flashed, 0)
        energy_levels = infos_for_next_stop[0]
        total_no_of_flashes += infos_for_next_stop[1]
    print('total no of flashes after', steps, 'steps:', total_no_of_flashes)


def puzzle2():
    energy_levels = copy.deepcopy(puzzle_input)
    step = 0
    while True:
        step += 1
        energy_levels += 1  # increase energy level of each octopus
        flashed = np.array([[False for _ in line] for line in puzzle_input])
        infos_for_next_stop = model_energy_levels(energy_levels, flashed, 0)
        energy_levels = infos_for_next_stop[0]
        if np.all((energy_levels == 0)): break
    print('first step during which all octopi flash:', step)


puzzle1()
puzzle2()
