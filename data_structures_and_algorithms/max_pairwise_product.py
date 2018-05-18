# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

first_largest = 0
second_largest = 0
position_first = 0

for i in range(len(a)):
	if a[i] > first_largest:
		first_largest = a[i]
		position_first = i

for i in range(len(a)):
	if a[i] > second_largest and  i != position_first:
		second_largest = a[i]

print(first_largest * second_largest)
