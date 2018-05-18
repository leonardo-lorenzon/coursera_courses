# Uses python3

def height_tree(nodes, n):
	

	max_height = 0
	j = 0
	while j < n:
		if nodes[j] == nodes[j - 1]:
			j += 1
		else:
			height = 0
			k = nodes[j]
			while k != - 1:
				height += 1
				k = nodes[k]
			max_height = max(max_height, height)
			j += 1
	return max_height + 1





if __name__ == "__main__":
	n = int(input())
	nodes = list(map(int, input().split()))
	print(height_tree(nodes, n))
	