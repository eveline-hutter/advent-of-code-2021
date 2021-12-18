with open('input17.txt') as file: puzzle_input = file.readline().replace('target area: x=', '')

x_area, y_area = puzzle_input.split(', y=')
x_from, x_to = [int(x) for x in x_area.split('..')]
y_from, y_to = [int(y) for y in y_area.split('..')]
max_y = 0


def probe(probe_position_x, probe_position_y, velocity_x, velocity_y, steps):
    for step in range(steps):
        probe_position_x += velocity_x
        probe_position_y += velocity_y
        if velocity_x > 0: velocity_x -= 1
        elif velocity_x < 0: velocity_x += 1
        velocity_y -= 1
        if x_from <= probe_position_x <= x_to and y_from <= probe_position_y <= y_to:
            return True
    return False


def max_y(velocity):
    return int(velocity * (velocity + 1) / 2)


def puzzle1():
    global max_y
    start_x, start_y = 0, 0
    initial_velocity_x, initial_velocity_y = 200, 500
    while True:
        for velocity_y in range(initial_velocity_y, 0, -1):
            for velocity_x in range(initial_velocity_x, 0, -1):
                if probe(start_x, start_y, velocity_x, velocity_y, 300):
                    print('highest y position:', max_y(velocity_y), 'max_y = ', velocity_y)
                    max_y = velocity_y
                    return


def puzzle2():
    start_x, start_y = 0, 0
    initial_velocity_x, initial_velocity_y = 1000, max_y    # 92
    no_of_velocity_values = 0
    for velocity_y in range(initial_velocity_y, - 500, -1):
        for velocity_x in range(initial_velocity_x, -500, -1):
            if probe(start_x, start_y, velocity_x, velocity_y, 300):
                no_of_velocity_values += 1
    print(no_of_velocity_values)


puzzle1()
puzzle2()
