f = open("input.txt", "r")
fr = f.read()

lines = fr.split('\n')[:-1]

# defining maximums
m_red, m_green, m_blue = (12, 13, 14)

possibles_sum = 0

for line in lines:
	game, bags = line.split(':')
	game_n = int(game.split(' ')[1])
	bags = bags.split(';')
	game_possible = True
	for bag in bags:
		cubes = {'red': 0,
		'green':0,
		'blue':0}
		items = bag.split(', ')
		for item in items:
			count, color = item.split()
			cubes[color] = int(count)
		# verifiy
		if cubes['red'] > m_red or cubes['green'] > m_green or cubes['blue'] > m_blue:
			game_possible = False
			break
	if(game_possible):
		possibles_sum +=  game_n
		
print(possibles_sum)
	
