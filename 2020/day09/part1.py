puzzle_input = [int(s.strip()) for s in open('input.in').readlines()]

preamble = puzzle_input[:25]

for i in puzzle_input[25:]:
    valid = False
    for j in preamble:
        if i-j in preamble:
            valid = True
    if not valid:
        print("first invalid:", i)
        exit()
    preamble.pop(0)
    preamble.append(i)
