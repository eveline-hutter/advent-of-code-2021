import copy

with open('input4.txt') as file:
    input_orig = file.readlines()

input_str = [str(line).replace("  ", " ") for line in input_orig[2:]]
input = []
# remove spaces in front of single numbers and \n at the end of each line
for line in input_str:
    clipped_line = ''
    if line[0] == ' ':
        clipped_line = line[1:]
    else:
        clipped_line = line
    input.append(clipped_line.replace("\n", ""))

called_numbers = [int(x) for x in input_orig[0].split(",")]


def create_bingo_sheets(input_nrs):
    bingo_sheets = []
    sheet = []
    for line in input_nrs:
        if line == '':
            bingo_sheets.append(sheet)
            sheet = []
        else:
            sheet.append([int(x) for x in line.split(" ")])
    return bingo_sheets


def check_if_line_full(sheet, row, col):
    # check rows
    row_counter = 0
    for nr in sheet[row]:
        if nr == -1:
            row_counter += 1
    if row_counter == 5:
        return True
    else:        # check columns
        col_counter = 0
        for i in range(len(sheet)):
            if sheet[i][col] == -1:
                col_counter += 1
        if col_counter == 5:
            return True
    return False


def calculate_unmarked_nrs(sheet):
    unmarked_nrs = 0
    for i in range(len(sheet)):
        for j in range(len(sheet[i])):
            nr = sheet[i][j]
            if nr != -1:
                unmarked_nrs += nr
    return unmarked_nrs


def puzzle1():
    bingo_sheets = create_bingo_sheets(input)
    bingo_doubles = copy.deepcopy(bingo_sheets)    # copy bingo sheets

    # check if nr is on sheets
    for nr in called_numbers:
        for x in range(len(bingo_sheets)):
            for i in range(len(bingo_sheets[x])):
                for j in range(len(bingo_sheets[x][i])):
                    if bingo_sheets[x][i][j] == nr:
                        bingo_doubles[x][i][j] = -1
                        if check_if_line_full(bingo_doubles[x], i, j):
                            print('bingo! called nr:', nr)
                            unmarked_nrs = calculate_unmarked_nrs(bingo_doubles[x])
                            print('winning board score:', unmarked_nrs * nr)
                            return


def puzzle2():
    bingo_sheets = create_bingo_sheets(input)
    bingo_doubles = copy.deepcopy(bingo_sheets)    # copy bingo sheets
    sheets_with_full_lines = [False for _ in range(len(bingo_sheets))]

    def only_one_sheet_left():
        for sheet in sheets_with_full_lines:
            if not sheet:
                return False
        return True

    # check if nr is on sheets
    for nr in called_numbers:
        for x in range(len(bingo_sheets)):
            for i in range(len(bingo_sheets[x])):
                for j in range(len(bingo_sheets[x][i])):
                    if bingo_sheets[x][i][j] == nr:
                        bingo_doubles[x][i][j] = -1
                        if check_if_line_full(bingo_doubles[x], i, j):
                            sheets_with_full_lines[x] = True
                            if only_one_sheet_left():
                                unmarked_nrs = calculate_unmarked_nrs(bingo_doubles[x])
                                print('winning board score:', unmarked_nrs * nr)
                                return


puzzle1()
puzzle2()
