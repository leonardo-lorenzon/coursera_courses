# Uses python3
import sys


def merge_lists(left_sublist,right_sublist):
	i,j = 0,0
	result = []
	#iterate through both left and right sublist
	while i<len(left_sublist) and j<len(right_sublist):
		#if left value is lower than right then append it to the result
		if left_sublist[i] <= right_sublist[j]:
			result.append(left_sublist[i])
			i += 1
		else:
			#if right value is lower than left then append it to the result
			result.append(right_sublist[j])
			j += 1
	#concatenate the rest of the left and right sublists
	result += left_sublist[i:]
	result += right_sublist[j:]
	#return the result
	return result

def merge_sort(input_list):
	#if list contains only 1 element return it
	if len(input_list) <= 1:
		return input_list
	else:
		#split the lists into two sublists and recursively split sublists
		midpoint = int(len(input_list)/2)
		left_sublist = merge_sort(input_list[:midpoint])
		right_sublist = merge_sort(input_list[midpoint:])
		#return the merged list using the merge_list function above
		return merge_lists(left_sublist,right_sublist)


def get_majority_element(a):
	if len(a) == 1:
		return 1

	a = merge_sort(a)
	cont = 1
	len_a = len(a)
	majority = len(a) // 2

	for i in range(1, len_a):
		if a[i] == a[i - 1]:
			cont += 1
		else:
			cont = 1

		if cont > majority:
			return 1

	return 0






if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a) == 1:
        print(1)
    else:
        print(0)
