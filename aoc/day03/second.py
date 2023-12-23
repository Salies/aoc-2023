f = open("aoc/day03/input.txt", "r")
fr = f.read()

lines = fr.split()

def get_neighbors(m, x, y):
    neighbors = []
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i >= 0 and j >= 0 and i < len(m) and j < len(m[i]):
                if i != x or j != y:
                    neighbors.append((m[i][j], i, j))
    return neighbors

# go looking left and right until it's not a number anymore
def expand_neighbor(m, i, j):
    # get left and right
    left = ''
    right = ''
    # search left
    v = j - 1
    while v >= 0 and m[i][v].isdigit():
        # add to the left of left
        left = m[i][v] + left
        v -= 1
    ll = v + 1
    # search right
    v = j + 1
    while v < len(m[i]) and m[i][v].isdigit():
        right += m[i][v]
        v += 1
    rl = v - 1
    num = left + m[i][j] + right
    return ((
        f'{num}-{ll}-{rl}',
        int(num)
        ))

nums_to_add = []
cumsum = 0

line_len = len(lines[0])
for i in range(len(lines)):
    for j in range(line_len):
        if lines[i][j] != '*':
            continue
        # get neighbors
        neighbors = get_neighbors(lines, i, j)
        # expand neighbors
        n_map = {}
        for neighbor in neighbors:
            if not neighbor[0].isdigit():
                continue
            n = expand_neighbor(lines, neighbor[1], neighbor[2])
            # if not in map, add to map
            if n[0] not in n_map:
                n_map[n[0]] = n[1]
        # if number of keys is map is less than 2, skip
        if len(n_map) < 2:
            continue
        # else, calculate product
        prod = 1
        for key in n_map:
            prod *= n_map[key]
        # add to cumulative sum
        cumsum += prod
    
print(cumsum)