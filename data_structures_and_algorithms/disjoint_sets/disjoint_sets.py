class DisjointSets:
	def __init__(self, n):
		self.parent = [0 for x in range(n + 1)]
		self.rank = [0 for x in range(n + 1)]

	def Make_set(self, i):
		self.parent[i] = i
		self.rank[i] = 0

	def Find(self, i):
		if i != self.parent[i]:
			self.parent[i] = self.Find(self.parent[i])
		return self.parent[i]

	def Union(self, i, j):
		i_id = self.Find(i)
		j_id = self.Find(j)

		if i_id == j_id:
			return
		if self.rank[i_id] > self.rank[j_id]:
			self.parent[j_id] = i_id
		else:
			self.parent[i_id] = j_id
			if self.rank[i_id] == self.rank[j_id]:
				self.rank[j_id] = self.rank[i_id] + 1

	def output(self):
		return self.rank

#Execution

s = DisjointSets(61)
for i in range(1,61):
	s.Make_set(i)
for i in range(1,31):
	s.Union(i, 2*i)
for i in range(1,21):
	s.Union(i,i*3)
for i in range(1,13):
	s.Union(i,i*5)
for i in range(1,61):
	s.Find(i)

print(s.output())
print(s.parent)