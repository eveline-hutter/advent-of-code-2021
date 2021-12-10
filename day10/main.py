import copy

with open('input10.txt') as file: puzzle_input = [list(line) for line in file.read().splitlines()]    # open without /n

opening_characters, closing_characters, syntax_errors = ['(', '[', '{', '<'], [')', ']', '}', '>'], [3, 57, 1197, 25137]
incomplete_lines = []


def puzzle1():
    def check_line(line):
        if len(line) == 0:
            print('all is fine and dandy')
            return True
        # find first closing character in line
        first_closing_char_index = -1
        first_closing_char_index_in_collection = -1
        closing_char = ''
        for i in range(len(line)):
            char = line[i]
            if closing_characters.__contains__(char):
                first_closing_char_index = i
                first_closing_char_index_in_collection = closing_characters.index(char)
                closing_char = char
                break
        opening_char = line[first_closing_char_index - 1]
        if opening_char == opening_characters[first_closing_char_index_in_collection]:
            line.pop(first_closing_char_index)
            line.pop(first_closing_char_index - 1)
            return check_line(line)
        else:
            if closing_char != '':
                # line is corrupted
                return syntax_errors[first_closing_char_index_in_collection]
            else:
                # line is incomplete
                return False
    puzzle_input_copy = copy.deepcopy(puzzle_input)
    total_syntax_error_score = 0
    for i in range(len(puzzle_input_copy)):
        syntax_error_score = check_line(puzzle_input_copy[i])
        if not syntax_error_score: incomplete_lines.append(puzzle_input[i])
        else: total_syntax_error_score += syntax_error_score
    print('total syntax error score:', total_syntax_error_score)


def puzzle2():
    def check_line(line, addings):
        if len(line) == 0:
            print('all is fine and dandy')
            return addings
        # find first closing character in line
        first_closing_char_index = -1
        first_closing_char_index_in_collection = -1
        for i in range(len(line)):
            char = line[i]
            if closing_characters.__contains__(char):
                first_closing_char_index = i
                first_closing_char_index_in_collection = closing_characters.index(char)
                break
        if first_closing_char_index != -1:
            opening_char = line[first_closing_char_index - 1]
            if opening_char == opening_characters[first_closing_char_index_in_collection]:
                line.pop(first_closing_char_index)
                line.pop(first_closing_char_index - 1)
                return check_line(line, addings)
            else:
                opening_char_index = opening_characters.index(opening_char)
                expected_closing_char = closing_characters[opening_char_index]
                line.insert(first_closing_char_index, expected_closing_char)
                return check_line(line, addings.append(opening_char))
        else:
            for i in range(len(line) - 1, -1, -1):
                opening_char = line[i]
                addings.append(opening_char)
            return addings

    def count_score(addings):
        score = 0
        for adding in addings:
            score *= 5
            if adding == '(':
                score += 1
            elif adding == '[':
                score += 2
            elif adding == '{':
                score += 3
            elif adding == '<':
                score += 4
            else:
                print('could not identify adding', adding)
        return score

    autocompletions = []
    for line in incomplete_lines:
        addings = check_line(line, [])
        if addings:
            autocompletions.append(count_score(addings))
    autocompletions = sorted(autocompletions)
    middle_index = int((len(autocompletions) - 1) / 2)
    print('middle autocompletion score:', autocompletions[middle_index])


puzzle1()
puzzle2()
