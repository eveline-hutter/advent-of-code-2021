with open('input2.txt') as file:
    input = file.readlines()

directions = []
distances = []

for line in input:
    instructions = line.split(' ')
    directions.append(instructions[0])
    distances.append(int(instructions[1]))


def puzzle1():
    horizontal = 0
    vertical = 0
    for i in range(len(input)):
        direction = directions[i]
        distance = distances[i]
        if direction == 'forward':
            horizontal += distance
        elif direction == 'down':
            vertical += distance
        elif direction == 'up':
            vertical -= distance
        else:
            print('could not identify direction:', direction)
    print('horizontal:', horizontal, 'vertical:', vertical, 'total', horizontal * vertical)


def puzzle2():
    horizontal = 0
    vertical = 0
    aim = 0
    for i in range(len(input)):
        direction = directions[i]
        distance = distances[i]
        if direction == 'forward':
            horizontal += distance
            vertical += aim * distance
        elif direction == 'down':
            aim += distance
        elif direction == 'up':
            aim -= distance
        else:
            print('could not identify direction:', direction)
    print('horizontal:', horizontal, 'vertical:', vertical, 'aim:', aim, 'total', horizontal * vertical)


puzzle1()
puzzle2()
