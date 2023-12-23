f = open("aoc/day04/input.txt", "r")
fr = f.read()

lines = fr.strip().split('\n')

psum = 0
for line in lines:
    _, info = line.split(':')
    winning, have = info.strip().split('|')
    winning = winning.split()
    have = have.split()
    # the C way would be sorting both lists and then comparing them with an algo
    # but I'm gonna trust Python with this one
    n = len(set(winning).intersection(have)) - 1
    points = 0
    if n > -1:
        points = 1 << n
    psum += points

print(psum)