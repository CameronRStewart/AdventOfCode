p = '/Users/bacchus/Documents/Code/coding-challenges/:r:codefoo/AdventOfCode/InputFiles/day_3.txt'

# A claim like
#
# #123 @ 3,2: 5x4
#
# ID 123
# 3 inches from the left edge,
# 2 inches from the top edge,
# 5 inches wide,
# 4 inches tall


# How many square inches of fabric are within two or more claims?


def map_claims(p):
    vertex_vals = {}
    total_overlap = 0
    with open(p) as fp:
        for line in fp:
            components = line.split(' ')
            id = components[0][1:]
            (from_left, from_top) = components[2].split(',')
            from_left = int(from_left)
            from_top = int(from_top[:-1])
            (wide, tall) = components[3].split('x')
            wide = int(wide)
            tall = int(tall)
            for i in range(from_left, from_left + wide):
                for j in range(from_top, from_top + tall):
                    dict_index = str(i) + "," + str(j)
                    if dict_index in vertex_vals:
                        if vertex_vals[dict_index][0] == 1:
                            total_overlap += 1
                        vertex_vals[dict_index][0] += 1
                        vertex_vals[dict_index][1].append(id)
                    else:
                        vertex_vals[dict_index] = [1, [id]]
    print(total_overlap)
    return total_overlap


map_claims(p)