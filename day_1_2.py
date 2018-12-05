p = '/Users/bacchus/Documents/Code/coding-challenges/:r:codefoo/AdventOfCode/InputFiles/day_1_1.txt'
p2 = '/Users/bacchus/Documents/Code/coding-challenges/:r:codefoo/AdventOfCode/InputFiles/day_1_2b.txt'

def get_first_repeated_frequency(path):
    f = open(path, 'r+')
    frequencies = [int(line) for line in f.readlines()]
    frequencies_so_far = set()
    sum = 0
    keep_going = True
    while keep_going:
        for freq in frequencies:
            sum += freq
            if sum in frequencies_so_far:
                return sum
            else:
                frequencies_so_far.add(sum)