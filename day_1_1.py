


p = '/Users/bacchus/Documents/Code/coding-challenges/:r:codefoo/AdventOfCode/InputFiles/day_1_1.txt'

def get_frequencies(path):
    f = open(path, 'r+')
    frequencies = [int(line) for line in f.readlines()]
    result = sum(frequencies)
    return result
