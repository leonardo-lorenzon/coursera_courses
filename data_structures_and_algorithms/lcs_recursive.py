def lcs(s1, s2, x = None, y = None):
	if x == None:
		x = len(s1) - 1
		y = len(s2) - 1


	if x == - 1 or y == -1:
		return 0
	else:
		if s1[x] == s2[y]:
			return 1 + lcs(s1, s2, x - 1, y - 1)
		else:
			return max(lcs(s1,s2,x - 1, y), lcs(s1, s2, x, y - 1))