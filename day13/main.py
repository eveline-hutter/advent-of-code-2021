simport numpy as np
import copy

with open('input13.txt') as file: puzzle_input = file.read().splitlines()  # open without /n

# create the original paper sheet
dots_until = puzzle_input.index('')
dots = puzzle_input[:dots_until]
dots_x, dots_y = [int(line.split(',')[0]) for line in dots], [int(line.split(',')[1]) for line in dots]
paper_sheet = np.zeros((max(dots_y) + 1, max(dots_x) + 1), dtype=int)
for i in range(len(dots)):
    paper_sheet[dots_y[i]][dots_x[i]] = 1

folding_instructions = [instruction.strip('fold along ') for instruction in puzzle_input[dots_until + 1:]]
folding_axes, folding_lines = [line.split('=')[0] for line in folding_instructions], [int(line.split('=')[1]) for line in folding_instructions]


def fold(sheet, folding_axis, folding_line):
    if folding_axis == 'y':
        origami = sheet[0:folding_line, :]
        folding = np.flipud(sheet[folding_line + 1:, :])
    else:
        origami = sheet[:, 0:folding_line]
        folding = np.fliplr(sheet[:, folding_line + 1:])
    # adding 1 for each dot to the sheet instead of just setting visible dots to 1
    # because I thought it would be needed for the second puzzle (ink density or whatever)
    # ... turned out, it wasn't needed after all
    return origami + folding


def puzzle1():
    origami = np.array(paper_sheet)
    for i in range(len(folding_instructions[:1])):
        origami_copy = copy.deepcopy(origami)
        origami = fold(origami_copy, folding_axes[i], folding_lines[i])
    print('visible dots after first folding:', np.count_nonzero(origami))


def puzzle2():
    origami = np.array(paper_sheet)
    for i in range(len(folding_instructions)):
        origami_copy = copy.deepcopy(origami)
        origami = fold(origami_copy, folding_axes[i], folding_lines[i])
    # the shape of the final origami is (6, 40), so each of the 8 letters is of shape (6, 5)
    # finding that the fifth row of each letter only consists of zeros, I only print shapes (6, 4)
    # now you have to manually (that is, visually) decode the letters ... resulting in AHGCPGAU
    for i in range(0, len(origami[0]), 5):
        letter = origami[:, i:i+4]
        print(letter)
        print()
        print()


puzzle1()
puzzle2()
