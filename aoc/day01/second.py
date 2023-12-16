from collections import deque

patterns = [
    '1', 'one',
    '2', 'two',
    '3', 'three',
    '4', 'four',
    '5', 'five',
    '6', 'six',
    '7', 'seven',
    '8', 'eight',
    '9', 'nine'
]

# A possible average case optimization would be to start
# searching at the end of the string for the last occurrence

mapping = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

class TrieNode:
    def __init__(self):
        self.children = {}
        self.output = []
        self.failure = None

def build_trie(patterns):
    root = TrieNode()
    for pattern in patterns:
        node = root
        for char in pattern:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.output.append(pattern)
    return root

def build_failure_function(root):
    queue = deque()
    for node in root.children.values():
        queue.append(node)
        node.failure = root

    while queue:
        current_node = queue.popleft()
        for char, child in current_node.children.items():
            queue.append(child)
            failure_node = current_node.failure
            while failure_node and char not in failure_node.children:
                failure_node = failure_node.failure
            child.failure = failure_node.children[char] if failure_node else root
            child.output += child.failure.output

def aho_corasick(text, root):
    current_node = root
    matches = []

    for i, char in enumerate(text):
        while current_node and char not in current_node.children:
            current_node = current_node.failure

        if not current_node:
            current_node = root
            continue

        current_node = current_node.children[char]

        for pattern in current_node.output:
            matches.append(pattern)

    return matches
    
def first_last(text, root):
	result = aho_corasick(text, root)
	first, last = result[0], result[-1]
	mf, ml = mapping.get(first), mapping.get(last)
	if mf is not None:
		first = mf
	if ml is not None:
		last = ml
	
	return int(first + last)

f = open("input.txt", "r")
fr = f.read()
lines = fr.split()

root = build_trie(patterns)
build_failure_function(root)

casum = 0
for line in lines:
	num = first_last(line, root)
	casum += num
print(casum)

