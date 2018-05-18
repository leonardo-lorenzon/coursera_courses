# Uses python3

def brackets_match(s):
	len_s = len(s)
	bracket_array = []

	for i in range(len_s):
		if s[i] == "(" or s[i] == "[" or s[i] == "{":
			bracket_array.append(s[i])
			first = i + 1

		if s[i] == ")" or s[i] == "]" or s[i] == "}":
			if len(bracket_array) == 0:
				return i + 1
			top = bracket_array.pop()
			first -= 1
			if (top == "[" and s[i] != "]")  or (top == "(" and s[i] != ")") or (top == "{" and s[i] != "}"):
				return i + 1

	if len(bracket_array) != 0:
				return first

	return "Success"


if __name__ == '__main__':
	s = input()
	print(brackets_match(s))