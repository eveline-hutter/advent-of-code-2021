import copy
import math

with open('input18.txt') as file: puzzle_input = file.read().splitlines()   # open without /n


def find_depths(number):
    depths = []
    for i in range(len(number)):
        if number[i].isnumeric():
            depth = number[:i].count('[') - number[:i].count(']')
            depths.append([int(number[i]), depth])
    return depths


def add_snailfish_numbers(no1, no2):
    snailfish_sum = []
    for element in no1: snailfish_sum.append(element)
    for element in no2: snailfish_sum.append(element)
    for element in snailfish_sum: element[1] += 1
    continuing = True
    while continuing:
        continuing = False
        exploded = False
        for i in range(len(snailfish_sum)):
            if snailfish_sum[i][1] > 4:
                # explode
                left_element, right_element = snailfish_sum[i][0], snailfish_sum[i + 1][0]
                if i > 0:
                    snailfish_sum[i - 1][0] += left_element
                if i < len(snailfish_sum) - 2:
                    snailfish_sum[i + 2][0] += right_element
                snailfish_sum.pop(i)
                snailfish_sum[i][0] = 0
                snailfish_sum[i][1] -= 1
                exploded = True
                continuing = True
                break
        if not exploded:
            for i in range(len(snailfish_sum)):
                if snailfish_sum[i][0] > 9:
                    # split
                    left_element, right_element = math.floor(snailfish_sum[i][0] / 2), math.ceil(snailfish_sum[i][0] / 2)
                    new_depth = snailfish_sum[i][1] + 1
                    snailfish_sum[i] = [left_element, new_depth]
                    snailfish_sum.insert(i + 1, [right_element, snailfish_sum[i][1]])
                    continuing = True
                    break
    return snailfish_sum


def calculate_magnitude(number):
    for level in range(4, -1, -1):
        indices_to_remove = []
        for i in range(len(number) - 1):
            if number[i][1] == level and number[i+1][1] == level:
                left_element, right_element = number[i][0], number[i+1][0]
                magnitude = (3 * left_element + 2 * right_element)
                number[i] = [magnitude, level - 1]
                number[i+1] = [-1, -1]
                indices_to_remove.append(i+1)
        if indices_to_remove:
            for j in range(len(indices_to_remove)):
                indices_to_remove[j] -= j
                number.pop(indices_to_remove[j])
    return number[0][0]


def puzzle1():
    depths = [find_depths(line) for line in puzzle_input]
    result = copy.deepcopy(depths[0])
    for i in range(len(depths) - 1):
        result = add_snailfish_numbers(result, depths[i + 1])
    print('sum:', result)
    print('magnitude:', calculate_magnitude(result))


def puzzle2():
    depths = [find_depths(line) for line in puzzle_input]
    max_magnitude = 0
    for i in range(len(depths)):
        for j in range(len(depths)):
            if not i == j:
                numbers_to_sum = [copy.deepcopy(depths[i]), copy.deepcopy(depths[j])]
                snailfish_sum = add_snailfish_numbers(numbers_to_sum[0], numbers_to_sum[1])
                magnitude = calculate_magnitude(snailfish_sum)
                max_magnitude = max(max_magnitude, magnitude)
    print('max magnitude:', max_magnitude)


puzzle1()
puzzle2()
