f = open("input.txt", "r")
fr = f.read()

lines = fr.split('\n')[:-1]

psum = 0

for line in lines:
	game, bags = line.split(':')
	game_n = int(game.split(' ')[1])
	bags = bags.split(';')
	game_possible = True
	cubes = {'red': 0,
		'green':0,
		'blue':0}
	for bag in bags:
		items = bag.split(', ')
		for item in items:
			count, color = item.split()
			count = int(count)
			if count > cubes[color]:
				cubes[color] = count
	psum += (cubes['red'] * cubes['green'] * cubes['blue'])

print(psum)
	
