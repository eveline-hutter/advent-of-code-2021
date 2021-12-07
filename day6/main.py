with open('input6.txt') as file:
    puzzle_input = [int(x) for x in file.read().split(',')]


def puzzle1():
    # simulate lanternfish population recursively
    def simulate_lanternfish(population, duration):
        if duration == 0:
            print('lanternfish total:', len(population))
            return
        else:
            next_population = []
            for fish in population:
                if fish == 0:
                    next_population.append(6)  # parent fish
                    next_population.append(8)  # baby fish
                else:
                    next_population.append(fish - 1)
            return simulate_lanternfish(next_population, duration - 1)

    simulate_lanternfish(puzzle_input, 80)


def puzzle2():
    population = [puzzle_input.count(0), puzzle_input.count(1), puzzle_input.count(2), puzzle_input.count(3), puzzle_input.count(4),
                 puzzle_input.count(5), puzzle_input.count(6), puzzle_input.count(7), puzzle_input.count(8)]

    def simulate_lanternfish(fish_ages, duration):
        # simulate lanternfish population with an array holding the fish count for every age
        if duration == 0:
            print('lanternfish total:', sum(fish_ages))
            return
        else:
            parents_to_be = fish_ages[0]
            for i in range(len(fish_ages) - 1):
                fish_ages[i] = fish_ages[i + 1]     # age every fish

            fish_ages[6] += parents_to_be       # parent fish
            fish_ages[8] = parents_to_be        # baby fish
            return simulate_lanternfish(fish_ages, duration - 1)

    simulate_lanternfish(population, 256)


# puzzle1()
puzzle2()
