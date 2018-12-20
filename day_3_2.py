p = '/Users/bacchus/Documents/Code/coding-challenges/:r:codefoo/AdventOfCode/InputFiles/day_3.txt'

def non_overlapping_claims(p):
    vertex_vals = {}
    non_overlapped_index = {}
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
            # So far, this id doesnt have any overlaps (cause we havent done anything).
            non_overlapped_index[id] = 1
            for i in range(from_left, from_left + wide):
                for j in range(from_top, from_top + tall):
                    dict_index = str(i) + "," + str(j)
                    if dict_index in vertex_vals:
                        # both id and vertex_vals[dict_index][id] get removed from non_overlapped_index if they exist
                        if id in non_overlapped_index:
                            del non_overlapped_index[id]
                        if vertex_vals[dict_index] in non_overlapped_index:
                            del non_overlapped_index[vertex_vals[dict_index]]
                    else:
                        vertex_vals[dict_index] = id
    print(non_overlapped_index)

non_overlapping_claims(p)