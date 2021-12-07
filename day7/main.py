import sys

with open('input7.txt') as file:
    puzzle_input = [int(x) for x in file.read().split(',')]


def puzzle1():
    min_fuel_cost = sys.maxsize
    for i in range(max(puzzle_input)):
        min_fuel_cost = min(min_fuel_cost, sum([abs(i - crab) for crab in puzzle_input]))
    print('minimum fuel cost:', min_fuel_cost)


def puzzle2():
    def count_fuel_cost_exponentially(crabs, position):
        distances = [abs(position - crab) for crab in crabs]
        fuel_cost = [int(distance * (distance + 1) / 2) for distance in distances]
        return sum(fuel_cost)

    min_fuel_cost = sys.maxsize
    for i in range(max(puzzle_input)):
        min_fuel_cost = min(min_fuel_cost, count_fuel_cost_exponentially(puzzle_input, i))

    print('minimum fuel cost:', min_fuel_cost)


puzzle1()
puzzle2()
