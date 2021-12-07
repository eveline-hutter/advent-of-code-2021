import numpy as np

with open('input5.txt') as file:
    input = file.read().splitlines()    # open without /n

start_points = [line.split(' -> ')[0] for line in input]
end_points = [line.split(' -> ')[1] for line in input]
x1s = [int(line.split(',')[0]) for line in start_points]
y1s = [int(line.split(',')[1]) for line in start_points]
x2s = [int(line.split(',')[0]) for line in end_points]
y2s = [int(line.split(',')[1]) for line in end_points]
max_x = max(max(x1s), max(x2s))
max_y = max(max(y1s), max(y2s))


def draw_horziontal_line(field, x, y1, y2):
    for y in range(y1, y2 + 1):
        field[y][x] += 1


def draw_vertical_line(field, x1, x2, y):
    for x in range(x1, x2 + 1):
        field[y][x] += 1


def draw_diagonal_line(field, x1, y1, x2, y2):
    field[y1][x1] += 1
    if x2 == x1 or y2 == y1:
        return
    elif x1 < x2:
        return draw_diagonal_line(field, x1 + 1, y1 + 1, x2, y2) if y1 < y2 else draw_diagonal_line(field, x1 + 1, y1 - 1, x2, y2)
    else:
        return draw_diagonal_line(field, x1 - 1, y1 + 1, x2, y2) if y1 < y2 else draw_diagonal_line(field, x1 - 1, y1 - 1, x2, y2)


def count_overlaps(field):
    overlaps = 0
    for row in field:
        for point in row:
            if point >= 2:
                overlaps += 1
    return overlaps


def puzzle1():
    field = np.zeros((max_x + 1, max_y + 1))
    for i in range(len(input)):
        x1, x2, y1, y2 = x1s[i], x2s[i], y1s[i], y2s[i]
        # only continue if we have a horizontal (x1 = x2) or vertical (y1 = y2) line
        if x1 == x2:
            draw_horziontal_line(field, x1, min(y1, y2), max(y1, y2))
        if y1 == y2:
            draw_vertical_line(field, min(x1, x2), max(x1, x2), y1)
    print('overlaps:', count_overlaps(field))


def puzzle2():
    field = np.zeros((max_x + 1, max_y + 1))
    for i in range(len(input)):
        x1, x2, y1, y2 = x1s[i], x2s[i], y1s[i], y2s[i]
        # only continue if we have a horizontal (x1 = x2) or vertical (y1 = y2) line
        if x1 == x2:
            draw_horziontal_line(field, x1, min(y1, y2), max(y1, y2))
        elif y1 == y2:
            draw_vertical_line(field, min(x1, x2), max(x1, x2), y1)
        else:
            draw_diagonal_line(field, x1, y1, x2, y2)
    print('overlaps:', count_overlaps(field))


puzzle1()
puzzle2()
