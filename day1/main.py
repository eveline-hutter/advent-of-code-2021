with open('input1.txt') as file:
    input = [int(line) for line in file]

def puzzle1():
    increases = 0
    for i in range(len(input) - 1):
        if input[i] < input[i + 1]: increases += 1
    print(increases)

def puzzle2():
    increases = 0
    for i in range(len(input) - 3):
        sum1 = sum(input[i:i+3])
        sum2 = sum(input[i+1:i+4])
        if sum2 > sum1: increases += 1
    print(increases)

puzzle1()
puzzle2()