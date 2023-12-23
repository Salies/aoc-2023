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

i = 0

nums_to_add = []

while i < len(lines):
    j = 0
    buf = ''
    will_add = False
    while j < len(lines[i]):
        if lines[i][j].isdigit():
            if not will_add:
                # get neighbors
                neighbors = get_neighbors(lines, i, j)
                # if neighbor is not 0-9 or '.', will_add = True
                for neighbor in neighbors:
                    if neighbor != '.' and neighbor.isdigit() == False:
                        will_add = True
                        break
            buf += lines[i][j]
        else:
            if will_add:
                nums_to_add.append(int(buf))
            buf = ''
            will_add = False
        j += 1
    # do not ignore last in line
    if will_add and buf != '':
        nums_to_add.append(int(buf))
    i += 1

print(sum(nums_to_add))