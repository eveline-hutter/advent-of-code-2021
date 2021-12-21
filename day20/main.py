import numpy as np
from scipy import ndimage

with open('input20.txt') as file: puzzle_input = [list(line) for line in file.read().splitlines()]

enhancement_algorithm = puzzle_input[0]
input_img = puzzle_input[2:]
bool_img = np.array(input_img) == '#'


def find_output_pixel(nine_pixels):
    index_in_enhancement_algorithm = int(''.join('1' if pixel else '0' for pixel in nine_pixels), 2)
    output_pixel = enhancement_algorithm[index_in_enhancement_algorithm]
    return output_pixel == '#'


def enhance(steps):
    output_img = np.pad(bool_img, 1, mode='constant', constant_values=False)
    for _ in range(steps):
        output_img = ndimage.generic_filter(np.pad(output_img, 1, mode='edge'), find_output_pixel, size=(3,3), mode='nearest')
    print('lit pixels after', steps, 'steps:', np.count_nonzero(output_img))


def puzzle1():
    enhance(2)


def puzzle2():
    enhance(50)


puzzle1()
puzzle2()
