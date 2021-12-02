puzzle_input = open('input.in').readlines()

increase_count = 0

for i in range(1, len(puzzle_input)):
    prev = int(puzzle_input[i-1])
    next = int(puzzle_input[i])
    if next > prev:
        increase_count += 1

print("increase_count:", increase_count)