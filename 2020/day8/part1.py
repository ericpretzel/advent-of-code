puzzle_input = [s.strip().split(" ") for s in open('input.in').readlines()]

visited = []

acc = 0
i = 0
while i not in visited:
    visited.append(i)
    instruction = puzzle_input[i][0]
    num = int(puzzle_input[i][1])
    
    if instruction == 'acc':
        acc += num
        i += 1
    elif instruction == 'nop':
        i += 1
    elif instruction == 'jmp':
        i += num

print("accumulator:", acc)