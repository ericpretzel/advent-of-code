puzzle_input = open('input.in').readline().strip()

for i in range(14, len(puzzle_input)):
    prev = set(puzzle_input[i-14:i])
    if len(prev) == 14 and puzzle_input[i] not in prev:
        print(i)
        break

