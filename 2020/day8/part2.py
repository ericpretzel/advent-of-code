import copy
with open('input.in') as f:
    puzzle_input = [s.strip().split(" ") for s in f.readlines()]


# simulate, changing given instruction
def loop(change):
    # i h8 shallow copy
    changed_list = copy.deepcopy(puzzle_input)
    changed_list[change[0]][0] = change[1]
    visited = []
    acc = 0
    i = 0
    while i not in visited and i < len(puzzle_input):
        visited.append(i)
        instruction = changed_list[i][0]
        num = int(changed_list[i][1])
        
        if instruction == 'acc':
            acc += num
            i += 1
        elif instruction == 'nop':
            i += 1
        elif instruction == 'jmp':
            i += num
    if i == len(puzzle_input):
        return acc
    return -1

for i in range(len(puzzle_input)):
    if puzzle_input[i][0] == 'nop':
        change = (i, 'jmp')
    elif puzzle_input[i][0] == 'jmp':
        change = (i, 'nop')
    else: continue
    acc = loop(change)
    if acc >= 0: 
        print("accumulator:", acc)
        exit()