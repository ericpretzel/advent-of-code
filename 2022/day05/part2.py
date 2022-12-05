puzzle_input = [line for line in open('input.in').readlines()]

crates = []
for i in range(9): crates.append([])
i = 0

while True:
    line = puzzle_input[i]
    i += 1
    if line == "\n": break
    for j in range(1, len(line), 4):
        print(j, line[j])
        if line[j].isalpha():
            crates[(j-1)//4].insert(0, line[j])

while i < len(puzzle_input):
    print(crates)
    line = puzzle_input[i]
    amt, src, dst = map(int, line.split(" ")[1::2])
    crates[dst-1].extend(crates[src-1][-amt:])
    del crates[src-1][-amt:]
    i += 1

for c in crates:
    print(c[-1], end='')
print()
