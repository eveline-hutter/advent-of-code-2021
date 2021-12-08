import copy

with open('input8.txt') as file:
    puzzle_input = file.read().splitlines()    # open without /n

input_values = [line.split(' | ')[0] for line in puzzle_input]
output_values = [line.split(' | ')[1] for line in puzzle_input]


def puzzle1():
    # unique numbers are (no of segments in brackets)
    # 1 (2), 4 (4), 7 (3), 8 (7)
    segments_for_unique_numbers = [2, 4, 3, 7]
    unique_numbers = 0
    for output in output_values:
        for digit in output.split(' '):
            if segments_for_unique_numbers.__contains__(len(digit)):
                unique_numbers += 1
    print(unique_numbers)


def puzzle2():
    def diff(a, b):
        return list(set(a) - set(b)) + list(set(b) - set(a))

    def add_to_digit(digit, x):
        copy_digit = copy.deepcopy(digit)
        copy_digit.append(x)
        return sorted(copy_digit)

    def find_digit_in_output(digit, collection):
        for i in range(len(collection)):
            if len(diff(digit, collection[i])) == 0: return i

    # think the seven sinking steps!
    training_digits = [sorted(digit.split(' '), key=lambda elem: (len(elem), elem)) for digit in input_values]
    test_digits = [list(digit.split(' ')) for digit in output_values]
    output_sum = 0
    for j in range(len(training_digits)):
        digits = [list(sorted(digit)) for digit in training_digits[j]]
        no_1 = digits[0]
        no_7 = digits[1]
        no_4 = digits[2]
        no_8 = digits[9]
        aaa = diff(no_7, no_1)[0]
        no_4_and_aaa = add_to_digit(no_4, aaa)
        ggg = ''
        no_9 = ()
        for i in range(6, 9):
            possible_no_9 = digits[i]
            difference = diff(possible_no_9, no_4_and_aaa)
            if len(difference) == 1: no_9, ggg = possible_no_9, difference[0]
        ddd = ''
        no_3 = ()
        no_1_and_aaa_ggg = add_to_digit(add_to_digit(no_1, aaa), ggg)
        for i in range(3, 6):
            possible_no_3 = digits[i]
            difference = diff(possible_no_3, no_1_and_aaa_ggg)
            if len(difference) == 1: no_3, ddd = possible_no_3, difference[0]
        no_1_and_ddd = add_to_digit(no_1, ddd)
        bbb = diff(no_4, no_1_and_ddd)[0]
        fff = ''
        no_5 = ()
        aaa_bbb_ddd_ggg = sorted(list([aaa, bbb, ddd, ggg]))
        for i in range(3, 6):
            possible_no_5 = digits[i]
            difference = diff(possible_no_5, aaa_bbb_ddd_ggg)
            if len(difference) == 1: no_5, fff = possible_no_5, difference[0]
        ccc = diff(no_1, fff)[0]
        eee = diff(no_8, sorted(list([aaa, bbb, ccc, ddd, fff, ggg])))[0]
        no_0 = [aaa, bbb, eee, ggg, ccc, fff]
        no_2 = [aaa, ccc, ddd, eee, ggg]
        no_6 = [aaa, bbb, eee, ggg, fff, ddd]
        digit_collection = list([no_0, no_1, no_2, no_3, no_4, no_5, no_6, no_7, no_8, no_9])
        output = "".join([str(find_digit_in_output(value, digit_collection)) for value in test_digits[j]])
        output_sum += int(output)
    print('tadaa! the sum of all output values is', output_sum)


puzzle1()
puzzle2()
