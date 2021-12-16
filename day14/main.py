from collections import defaultdict, Counter
from pathlib import Path

with open('input14.txt') as file: puzzle_input = file.read().splitlines()   # open without /n

polymer_template = puzzle_input[0]
pair_insertions = puzzle_input[2:]
pairs, insertions = [insertion.split(' -> ')[0] for insertion in pair_insertions], [insertion.split(' -> ')[1] for insertion in pair_insertions]
insertion_dict, rules = {}, {}  #insertion dict is used in puzzle 1 and rules in puzzle 2
for i in range(len(pair_insertions)):
    insertion_dict[pairs[i]] = pairs[i][0] + insertions[i] + pairs[i][1]
    rules[pairs[i]] = insertions[i]


def insert(pair):
    return insertion_dict.get(pair)


def grow_polymer(steps):
    template_pairs = [str(polymer_template[i] + polymer_template[i+1]) for i in range(len(polymer_template) - 1)]
    resulting_polymer = ''
    for _ in range(steps):
        polymer = []
        for i in range(len(template_pairs)):
            output = insert(template_pairs[i])
            # only insert the whole trio the first time to avoid duplications
            if i == 0:
                polymer.append(output)
            else:
                polymer.append(output[1:])
        resulting_polymer = ''.join(polymer)
        template_pairs = [str(resulting_polymer[i] + resulting_polymer[i+1]) for i in range(len(resulting_polymer) - 1)]
    return resulting_polymer


def count_occurrences(polymer):
    unique_elements = list(set(polymer))
    return sorted([polymer.count(element) for element in unique_elements])


def puzzle1():
    polymer = grow_polymer(10)
    occurrences = count_occurrences(polymer)
    print(occurrences[-1] - occurrences[0])


def puzzle2():
    def count_occurences(steps):
        template_pairs = [str(polymer_template[i] + polymer_template[i + 1]) for i in range(len(polymer_template) - 1)]
        unique_element_counter = Counter(polymer_template)
        polymer_counter = Counter(template_pairs)
        for _ in range(steps):
            current_dict = defaultdict(int)
            for key in polymer_counter.keys():
                current_dict[key[0] + rules[key]] += polymer_counter[key]
                current_dict[rules[key] + key[1]] += polymer_counter[key]
                unique_element_counter[rules[key]] += polymer_counter[key]
            polymer_counter = current_dict
        return unique_element_counter.most_common()[0][1] - unique_element_counter.most_common()[-1][1]

    print(count_occurences(40))


puzzle1()
puzzle2()
