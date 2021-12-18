import copy
import math

# get binaries with leading zeros by prepending 1 to the hex no
with open('input16.txt') as file: puzzle_input = [bin(int('1' + line, 16)).replace('0b1', '') for line in file.read().splitlines()]

version_counter = 0


def get_literal_value(packet):
    groups = [packet[step:step + 5] for step in range(0, len(packet), 5)]
    value = ''
    remaining_groups = copy.deepcopy(groups)
    for group in groups:
        if len(group) == 5:
            value += group[1:]
            remaining_groups.remove(group)
            if group[0] == '0':
                break
    return int(value, 2), ''.join(remaining_groups)


def check_value(type_id, values):
    if type_id == 0: return sum(values)
    if type_id == 1: return math.prod(values)
    if type_id == 2: return min(values)
    if type_id == 3: return max(values)
    if type_id == 5:
        if values[0] > values[1]: return 1
        else: return 0
    if type_id == 6:
        if values[0] < values[1]: return 1
        else: return 0
    if type_id == 7:
        if values[0] == values[1]: return 1
        else: return 0


def decode_packet(packet):
    global version_counter
    version, type_id = int(packet[0:3], 2), int(packet[3:6], 2)
    version_counter += version
    payload = packet[6:]
    # parse literal values
    if type_id == 4:
        return get_literal_value(payload)
    # parse operators
    else:
        length_type_id = payload[0]
        if length_type_id == '0':
            subpackets_length = int(payload[1:16], 2)
            subpackets = payload[16:16 + subpackets_length]
            remaining = subpackets
            values = []
            while remaining:
                value, remaining = decode_packet(remaining)
                values.append(value)
            return check_value(type_id, values), payload[16 + subpackets_length:]
        else:
            no_of_subpackets = int(payload[1:12], 2)
            subpackets = payload[12:]
            subpackets_parsed = 0
            remaining = subpackets
            values = []
            while subpackets_parsed < no_of_subpackets:
                subpackets_parsed += 1
                value, remaining = decode_packet(remaining)
                values.append(value)
            return check_value(type_id, values), remaining


def puzzle1():
    decode_packet(puzzle_input[0])
    print(version_counter)


def puzzle2():
    print(decode_packet(puzzle_input[0])[0])


puzzle1()
puzzle2()
