p = '/Users/bacchus/Documents/Code/coding-challenges/:r:codefoo/AdventOfCode/InputFiles/day_2_1.txt'
import functools


def correct(path):
    with open(path) as fp:
        lines = fp.readlines()
    for i in range(0, len(lines) - 1):
        for j in range(1, len(lines) - 1):
            same_chars = count_different_chars(lines[i], lines[j])
            if same_chars == 1:
                return (lines[i], lines[j])


def char_to_bit_array(s):
    bits = bin(int.from_bytes(s.encode(), 'big'))[2:]
    return bit_array_from_byte_string(bits.zfill(8 * ((len(bits) + 7) // 8)))


def bit_array_from_byte_string(s): # given a byte string - converts to an array of bits
    res = []
    for char in s:
        res.append(int(char))
    return res


def compare_bit_arrays(a1, a2): # compare single char byte array and give xor'd arrau
    res = []
    for i in range(0, len(a1) - 1):
        res.append(a1[i]^a2[i])
    return res


def is_different(a, b):
    ba = char_to_bit_array(a)
    bb = char_to_bit_array(b)
    compared_bit_array = compare_bit_arrays(ba, bb)
    result = functools.reduce(lambda x,y: x or y, compared_bit_array)
    return result


def count_different_chars(s1, s2):
    diff = 0
    for i in range(0, len(s1) - 1):
        if is_different(s1[i], s2[i]):
            diff += 1
    return diff
