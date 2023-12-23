f = open("aoc/day04/input.txt", "r")
fr = f.read()

lines = fr.strip().split('\n')

# preprocessing
matches = {}
cards = []
for idx, line in enumerate(lines):
    _, info = line.split(':')
    winning, have = info.strip().split('|')
    winning = winning.split()
    have = have.split()
    n = len(set(winning).intersection(have))
    matches[idx] = n
    cards.append(idx)

i = 0
while i < len(cards):
    card = cards[i]
    n_matches = matches[card]
    for j in range(n_matches):
        cards.append(card + j + 1)
    i += 1

print(len(cards))