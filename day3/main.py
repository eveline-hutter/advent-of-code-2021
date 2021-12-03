with open('input3.txt') as file:
    input_orig = [str(line) for line in file]
# remove /n character at the end of each line
input = []
for line in input_orig:
    input.append(list(line.replace("\n", "")))  # cast str to list = list of chars for string


def puzzle1():
    gamma_rate, epsilon_rate = str(), str()
    for pos in range(len(input[0])):
        zeroes, ones = 0, 0
        for i in range(len(input)):
            if input[i][pos] == '0':
                zeroes += 1
            else:
                ones += 1
        if zeroes > ones:
            gamma_rate += '0'
            epsilon_rate += '1'
        else:
            gamma_rate += '1'
            epsilon_rate += '0'
    gamma_rate_dec = int(gamma_rate, 2)
    epsilon_rate_dec = int(epsilon_rate, 2)
    power_consumption = gamma_rate_dec * epsilon_rate_dec
    print('gamma rate:', gamma_rate_dec, 'epsilon rate:', epsilon_rate_dec, 'power consumption:', power_consumption)


def puzzle2():
    def determine_most_common_at_position(numbers, position, oxygen_rating):
        # abort recursion if only one number is left
        if len(numbers) == 1:
            number = "".join(numbers[0])
            return number
        # count zeroes and ones of all numbers in current position
        zeroes, ones = 0, 0
        for i in range(len(numbers)):
            if numbers[i][position] == '0':
                zeroes += 1
            else:
                ones += 1
        if zeroes > ones:
            numbers_to_keep = keep_zeroes(numbers, position) if oxygen_rating else keep_ones(numbers, position)
        else:
            numbers_to_keep = keep_ones(numbers, position) if oxygen_rating else keep_zeroes(numbers, position)
        return determine_most_common_at_position(numbers_to_keep, position + 1, oxygen_rating)

    def keep_zeroes(numbers, position):
        numbers_to_keep = []
        for number in numbers:
            if number[position] == '0':
                numbers_to_keep.append(number)
        return numbers_to_keep

    def keep_ones(numbers, position):
        numbers_to_keep = []
        for number in numbers:
            if number[position] == '1':
                numbers_to_keep.append(number)
        return numbers_to_keep

    oxygen_generator_rating = int(determine_most_common_at_position(input, 0, True), 2)
    co2_scrubber_rating = int(determine_most_common_at_position(input, 0, False), 2)
    life_support_rating = oxygen_generator_rating * co2_scrubber_rating
    print('oxygen generator rating:', oxygen_generator_rating, 'co2 scrubber rating:', co2_scrubber_rating, 'life support rating:', life_support_rating)


puzzle1()
puzzle2()
