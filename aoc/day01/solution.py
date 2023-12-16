f = open("input.txt", "r")
fr = f.read()

lines = fr.split()

casum = 0
for line in lines:
	idx = 0
	while not line[idx].isdigit():
		idx += 1
	first = line[idx]
	last = ''
	idx += 1
	while idx < len(line):
		if(line[idx].isdigit()):
			last = line[idx]
		idx += 1
	if(last == ''):
		last = first
	num = int(first + last)
	casum += num
print(casum)

