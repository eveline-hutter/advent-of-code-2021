with open('input21.txt') as file: puzzle_input = file.read().splitlines()

p1_start, p2_start = int(puzzle_input[0].replace('Player 1 starting position: ', '')), int(puzzle_input[1].replace('Player 2 starting position: ', ''))


def roll_die(last_roll):
    return max(1, (last_roll + 1) % 101)


def play():
    player_1_turn = True
    p1_position, p2_position = p1_start, p2_start
    p1_score, p2_score = 0, 0
    winning_score = 1000
    last_roll = 0
    rolls = 0
    while p1_score < winning_score and p2_score < winning_score:
        movement = 0
        for _ in range(3):
            rolls += 1
            roll = roll_die(last_roll)
            movement += roll
            last_roll = roll
        if player_1_turn:
            p1_position = (p1_position + movement) % 10
            if p1_position == 0: p1_position = 10
            p1_score += p1_position
        else:
            p2_position = (p2_position + movement) % 10
            if p2_position == 0: p2_position = 10
            p2_score += p2_position
        player_1_turn = not player_1_turn
        if last_roll == 100: last_roll = 0
    print('p1 score:', p1_score, '| p2 score:', p2_score, '| rolls counter:', rolls)
    print('losing player score * rolls counter:', min(p1_score, p2_score) * rolls)


def quantum_play():
    rolls_possibilities = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
    worlds = {(p1_start, p2_start, 0, 0, True): 1}
    p1_wins, p2_wins = 0, 0
    while worlds:
        next_worlds = {}
        for (p1_position, p2_position, p1_score, p2_score, player_1_turn), world in worlds.items():
            for roll in range(3, 10):
                if player_1_turn:
                    p1_next_position = (p1_position + roll) % 10
                    p1_next_score = p1_score + (p1_next_position or 10)
                    if p1_next_score >= 21:
                        p1_wins += world * rolls_possibilities.get(roll)
                    else:
                        state = (p1_next_position, p2_position, p1_next_score, p2_score, not player_1_turn)
                        next_worlds[state] = next_worlds.get(state, 0) + world * rolls_possibilities.get(roll)
                else:
                    p2_next_position = (p2_position + roll) % 10
                    p2_next_score = p2_score + (p2_next_position or 10)
                    if p2_next_score >= 21:
                        p2_wins += world * rolls_possibilities.get(roll)
                    else:
                        state = (p1_position, p2_next_position, p1_score, p2_next_score, not player_1_turn)
                        next_worlds[state] = next_worlds.get(state, 0) + world * rolls_possibilities.get(roll)
        worlds = next_worlds
    print('p1 wins:', p1_wins, 'p2 wins:', p2_wins, 'player with more wins won:', max(p1_wins, p2_wins), 'times')


def puzzle1():
    play()


def puzzle2():
    quantum_play()


puzzle1()
puzzle2()
