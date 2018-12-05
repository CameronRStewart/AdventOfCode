p = '/Users/bacchus/Documents/Code/coding-challenges/:r:codefoo/AdventOfCode/InputFiles/day_2_1.txt'
def twice_and_thrice(path):
    twice = 0
    thrice = 0
    with open(path) as fp:
        for line in fp:
            chars_count = {}
            for char in line:
                # keep a dict of chars with their count
                if char in chars_count:
                    chars_count[char] += 1
                else:
                    chars_count[char] = 1
            if 2 in chars_count.values():
                twice += 1
            if 3 in chars_count.values():
                thrice += 1
    return twice * thrice
