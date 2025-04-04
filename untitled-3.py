first_line = input()
second_line = input()

dct_one = {}
dct_two = {}

for i in range(len(first_line)):
    if first_line[i] not in dct_one:
        dct_one[first_line[i]] = 1
    else:
        dct_one[first_line[i]] += 1
    if i < len(second_line) - 1:
        if s_line[i] not in dct_one:
            dct_one[first_line[i]] = 1
        else:
            dct_one[first_line[i]] += 1

