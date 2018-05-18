import re

def sum_number_doc():
    total_sum = 0
    list_num = []
    handle = open("texts/regex_sum_38460.txt")

    for line in handle:
        list_num.extend(re.findall("[0-9]+", line))

    for i in list_num:
        total_sum += int(i)

    return total_sum


print(sum_number_doc())
