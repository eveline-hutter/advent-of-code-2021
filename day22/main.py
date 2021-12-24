import numpy as np

with open('input22.txt') as file: puzzle_input = file.read().splitlines()

on_off_turns = [line.split(' ')[0] for line in puzzle_input]
x_ranges = [line.split(',')[0].split('=')[1] for line in puzzle_input]
x_from, x_to = [range.split('..')[0] for range in x_ranges], [range.split('..')[1] for range in x_ranges]
y_ranges = [line.split(',')[1].split('=')[1] for line in puzzle_input]
y_from, y_to = [range.split('..')[0] for range in y_ranges], [range.split('..')[1] for range in y_ranges]
z_ranges = [line.split(',')[2].split('=')[1] for line in puzzle_input]
z_from, z_to = [range.split('..')[0] for range in z_ranges], [range.split('..')[1] for range in z_ranges]
