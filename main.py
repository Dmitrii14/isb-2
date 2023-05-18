import math
import re

BIT = 128


def read_file(filename: str) -> str:
    result = ""
    with open(filename, 'r', encoding='UTF-8') as file:
        result = file.read()
    return result


def frequency_test(random_sequence: str) -> dict:
    counter = {
        '0': 0,
        '1': 0
    }
    for item in random_sequence:
        if item == '0':
            counter['0'] += 1
        elif item == '1':
            counter['1'] += 1
    return counter


def sequence_bits_test(random_sequence) -> bool:
    for i in range(len(random_sequence) - 1):
        if random_sequence[i] == random_sequence[i + 1]:
            return True
    return False


def get_max(lst: list) -> int:
    max = lst[0]
    for i in range(len(lst)):
        if lst[i] > max:
            max = lst[i]
    return max


def get_sum(v_1: int, v_2: int, v_3: int, v_4: int):
    quadro_x = 0
    quadro_x += (pow((v_1 - 16 * 0.2148), 2)) / (16 * 0.2148)
    quadro_x += (pow((v_2 - 16 * 0.3672), 2)) / (16 * 0.3672)
    quadro_x += (pow((v_3 - 16 * 0.2305), 2)) / (16 * 0.2305)
    quadro_x += (pow((v_4 - 16 * 0.1875), 2)) / (16 * 0.1875)
    return quadro_x


def get_max_length_block(random_sequence: str):
    lst = re.sub('([^ ]{8})', r'\1 ', random_sequence).replace('  ', ' ').split(' ')

    dict = {
        "<=1": 0,
        "=2": 0,
        "=3": 0,
        ">=4": 0
    }

    for i in range(len(lst) - 1):
        for j in range(len(lst[i]) - 1):
            longest_match = len(max(re.findall('1+', lst[i]), key=len))
            if longest_match <= 1:
                dict["<=1"] += 1
            elif longest_match == 2:
                dict["=2"] += 1
            elif longest_match == 3:
                dict["=3"] += 1
            elif longest_match >= 4:
                dict[">=4"] += 1
            break
    return dict["<=1"], dict["=2"], dict["=3"], dict[">=4"]


if __name__ == '__main__':
    random_sequence = read_file("random_sequence.txt")
    dictionary_count = frequency_test(random_sequence)
    frequency_zeros = dictionary_count['0'] / BIT
    frequency_ones = dictionary_count['1'] / BIT
    difference_the_received_frequencies = frequency_zeros - frequency_ones
    print(difference_the_received_frequencies)
    p_1 = difference_the_received_frequencies
    p_2 = math.erfc((abs(dictionary_count['1'] - 2 * BIT * frequency_ones * (1 - frequency_ones))) /
                    (2 * math.sqrt(2 * BIT) * frequency_ones * (1 - frequency_ones)))
    print(p_2)
    v_1, v_2, v_3, v_4 = get_max_length_block(random_sequence)
    p_3 = get_sum(v_1, v_2, v_3, v_4)
    print(p_3)
