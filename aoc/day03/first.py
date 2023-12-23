f = open("aoc/day03/input.txt", "r")
fr = f.read()

lines = fr.split()

def get_neighbors(m, x, y):
    neighbors = []
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i >= 0 and j >= 0 and i < len(m) and j < len(m[i]):
                if i != x or j != y:
                    neighbors.append(m[i][j])
    return neighbors

nums_to_add = []

for i in range(len(lines)):
    buf = ''
    will_add = False
    for j in range(len(lines[i])):
        if lines[i][j].isdigit():
            buf += lines[i][j]
            if will_add:
                continue
            # get neighbors
            neighbors = get_neighbors(lines, i, j)
            # if neighbor is not 0-9 or '.', will_add = True
            for neighbor in neighbors:
                if neighbor != '.' and neighbor.isdigit() == False:
                    will_add = True
                    break
            continue
        if will_add:
            nums_to_add.append(int(buf))
        buf = ''
        will_add = False
    # do not ignore last in line
    if will_add and buf != '':
        nums_to_add.append(int(buf))

print(sum(nums_to_add))