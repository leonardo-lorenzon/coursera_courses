# python3
def left_child(i):
	return 2*i + 1
def right_child(i):
	return 2*i + 2

def sift_down(i, size, arr, swaps_arr):

	max_index = i

	l = left_child(i)
	if l <= size and arr[max_index] > arr[l]:
		max_index = l
	
	r = right_child(i)
	if r <= size and arr[max_index] > arr[r]:
		max_index = r

	if i != max_index:
		arr[i], arr[max_index] = arr[max_index], arr[i]
		swaps_arr.extend([i, max_index])
		sift_down(max_index, size, arr, swaps_arr)


def build_heap(arr):
	swaps_arr = []

	size = len(arr) - 1
	for i in range(size // 2, -1, -1):
		sift_down(i, size, arr, swaps_arr)
		
	return swaps_arr

if __name__ == "__main__":
	n = int(input())
	arr = list(map(int, input().split()))
	swaps_arr = build_heap(arr)
	
	print(len(swaps_arr) // 2)
	for i in range(0, len(swaps_arr), 2):
		print(swaps_arr[i], swaps_arr[i + 1])
