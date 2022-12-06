puzzle_input = open('input.in').readline().strip()

for i in range(4, len(puzzle_input)):
    print(puzzle_input[i-4:i])
    prev = set(puzzle_input[i-4:i])
    if len(prev) == 4 and puzzle_input[i] not in prev:
        print(i)
        break

